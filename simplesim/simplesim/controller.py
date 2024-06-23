from .wp_visualizer import *
from .random_waypoints_generator import *
from .simulator import *
from sim_msgs.msg import Waypoints as WP
from syst_msgs.msg import Waypoints
from syst_msgs.srv import AdvService
import time
import numpy as np

class Controller(Node):
    def __init__(self):
        super().__init__('controller')

        self.cli = self.create_client(AdvService, '/advertisement_service')
        self.drone_id = self.declare_parameter('drone_id', 'drone_x').get_parameter_value().string_value
        self.wps_subscription = self.create_subscription(Waypoints, f'/{self.drone_id}/route', self.listener_callback, 10)
        self.get_logger().info('lISTENING TO: "%s"' % f'/{self.drone_id}/route')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AdvService.Request()

        self.req.drone_id = self.drone_id
        self.req.speed = self.declare_parameter('max_speed', 30.0).get_parameter_value().double_value
        self.req.tof = self.declare_parameter('tof', 50.0).get_parameter_value().double_value
        self.req.sweep_width = self.declare_parameter('sweep_width', 33.0).get_parameter_value().double_value
        self.req.coordx = self.declare_parameter('coordx', -200.0).get_parameter_value().double_value
        self.req.coordy = self.declare_parameter('coordy', 0.0).get_parameter_value().double_value

        self.get_logger().info('CALLING SERVICE')
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.callback)

        self.drone_wps = self.declare_parameter(
            'waypoints', ['nun']).get_parameter_value().string_array_value
        
        self.get_logger().info(f'drone_wps: {str(self.drone_wps)}')

        self.publisher_ = self.create_publisher(WP, 'wps', 10)

    def callback(self, future):
        response = future.result()
        self.get_logger().info(f'Result of service call: {response}')

    def listener_callback(self, msg):
        wps_array = np.array(msg.wps, dtype=np.float64).reshape((int)(len(msg.wps)/3), 3)
        self.get_logger().info(f'data received {wps_array}')
        self.send_msg(wps_array)

    def send_msg(self, drone_wps):
        self.get_logger().info('SENDING MESSAGE FROM CONTROLLER')
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
    controller= Controller()
    rclpy.spin(controller)

if __name__ == '__main__':
    main()
