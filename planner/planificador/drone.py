from syst_msgs.srv import AdvService
from syst_msgs.msg import Waypoints
import rclpy
from rclpy.node import Node

import numpy as np

drone_id = ''

class Drone(Node):

    def __init__(self):
        global drone_id

        super().__init__('Drone')
        self.cli = self.create_client(AdvService, 'adv_service')
        drone_id = self.declare_parameter('drone_id', 'drone_x').get_parameter_value().string_value
        self.wps_subscription = self.create_subscription(Waypoints, f'{drone_id}_wps', self.listener_callback, 10)
        self.get_logger().info('lISTENING TO: "%s"' % f'{drone_id}_wps')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AdvService.Request()

        self.req.drone_id = drone_id
        self.req.speed = self.declare_parameter('speed', 30.0).get_parameter_value().double_value
        self.req.tof = self.declare_parameter('tof', 50.0).get_parameter_value().double_value
        self.req.ancho_de_barrido = self.declare_parameter('ancho_de_barrido', 33.0).get_parameter_value().double_value
        self.req.coordx = self.declare_parameter('coordx', -200.0).get_parameter_value().double_value
        self.req.coordy = self.declare_parameter('coordy', 0.0).get_parameter_value().double_value

        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.callback)
        # rclpy.spin_until_future_complete(self, self.future)
        # return self.future.result()

    def callback(self, future):
        response = future.result()
        self.get_logger().info(f'Result of service call: {response}')

    def listener_callback(self, msg):
        global drone_id
        wps_array = np.array(msg.wps, dtype=np.float64).reshape((int)(len(msg.wps)/3), 3)
        self.get_logger().info(f'data received {wps_array}')

"""
class MinimalServer(Node):

    def __init__(self, dname: str):
        super().__init__('minimal_server_async')
        self.srv = self.create_service(Waypoints, f'{dname}_service', self.receive_wps_callback)
    
    def receive_wps_callback(self, request, response):
        global is_server_done
        wps_array = np.array(request.wps, dtype=np.float64).reshape((int)(len(request.wps)/3), 3)
        self.get_logger().info(f'data received {wps_array}')
        
        #print(wps_array)
        #print(f'las coord son {wps_array[0][0]} : {wps_array[0][1]}')

        response.ready = 1
        is_server_done = True
        return response


class MinimalSubscriber(Node):

    def __init__(self, dname: str):
        super().__init__('minimal_subscriber')
        #self.wps_subscription = self.create_subscription(Waypoints, f'{dname}_wps', self.listener_callback, 10)  #drone_id is already defined
        self.wps_subscription = self.create_subscription(Waypoints, f'{dname}_wps', self.listener_callback, 10)
        self.get_logger().info('lISTENING TO: "%s"' % f'{dname}_wps')

    def listener_callback(self, msg):
        global drone_id, wps_received
        wps_array = np.array(msg.wps, dtype=np.float64).reshape((int)(len(msg.wps)/3), 3)
        self.get_logger().info(f'data received {wps_array}')
        wps_received = True
"""
def main():
    global drone_id
    rclpy.init()

    rclpy.spin(Drone())

    rclpy.shutdown()

if __name__ == '__main__':
    main()