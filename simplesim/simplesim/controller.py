from .wp_visualizer import *
from .random_waypoints_generator import *
from .simulator import *
from sim_msgs.msg import Waypoints as WP
import time

import rclpy
from rclpy.node import Node
from syst_msgs.srv import AdvService, Waypoints

import numpy as np

drone_id = ''
wps_array = None
class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AdvService, '/adv_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AdvService.Request()

    def send_request(self):
        global drone_id
        drone_id = self.declare_parameter('drone_id', 'drone_x').get_parameter_value().string_value

        self.req.drone_id = drone_id
        self.req.speed = self.declare_parameter('max_speed', 30.0).get_parameter_value().double_value
        self.req.tof = self.declare_parameter('tof', 50.0).get_parameter_value().double_value
        self.req.ancho_de_barrido = self.declare_parameter('sweep_width', 33.0).get_parameter_value().double_value
        self.req.coordx = self.declare_parameter('coordx', -200.0).get_parameter_value().double_value
        self.req.coordy = self.declare_parameter('coordy', 0.0).get_parameter_value().double_value
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

is_server_done = False

class MinimalServer(Node):

    def __init__(self, dname: str):
        super().__init__('minimal_server_async')
        self.srv = self.create_service(Waypoints, f'{dname}_service', self.receive_wps_callback)
    
    def receive_wps_callback(self, request, response):
        global is_server_done, wps_array
        wps_array = np.array(request.wps, dtype=np.float64).reshape((int)(len(request.wps)/3), 3)
        self.get_logger().info(f'data received {wps_array}')
        
        #print(wps_array)
        #print(f'las coord son {wps_array[0][0]} : {wps_array[0][1]}')

        response.ready = 1
        is_server_done = True
        return response

class WpsPublisher(Node):
    def __init__(self):
        super().__init__('wps_publisher')
        global wps_array

        # self.drone_wps = self.declare_parameter(
        #     'waypoints', ['nun']).get_parameter_value().string_array_value
        
        # self.get_logger().info(f'drone_wps: {str(self.drone_wps)}')

        self.publisher_ = self.create_publisher(WP, 'wps', 1)
        self.send_msg(wps_array)

    def send_msg(self, drone_wps):
        wps = self.process_waypoints(drone_wps)

        time.sleep(0.5)

        wps_msg = WP()
        wps_msg.wps = wps

        self.publisher_.publish(wps_msg)

    def process_waypoints(self, drone_wps):
        '''
        Procesa el waypoint dado
        '''
        poses = []
        for waypoint_array in drone_wps:
            if isinstance(waypoint_array, str):
                waypoint = waypoint_array.split(";")
                self.get_logger().info('Waypoints in String format')
            else:
                waypoint = waypoint_array
                self.get_logger().info('Waypoints in array format')
            x = float(waypoint[0])
            y = float(waypoint[1])
            z = float(waypoint[2])
            
            newPos = PoseStamped()
            newPos.pose.position.x = x
            newPos.pose.position.y = y
            newPos.pose.position.z = z
            poses.append(newPos)

        return poses

    def random(self):
        return generate_random_waypoints(25, 10)

def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request()
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (12.3, 50.2, response.response))

    minimal_client.destroy_node()
    
    minimal_server = MinimalServer(drone_id)
    while not is_server_done:
        rclpy.spin_once(minimal_server)
    minimal_server.destroy_node()

    wps_publisher = WpsPublisher()
    rclpy.spin(wps_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()