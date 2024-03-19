from syst_msgs.srv import AdvService
from syst_msgs.msg import Waypoints
import rclpy
from rclpy.node import Node

from planning_algorithm.main import verdugo
from .wps_processation_tools import *

import os

i = 0
flight_height = 0
service_active = True
drones = []
wps_metadata = WPS_metadata()

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        
        global i, flight_height
        i = self.declare_parameter('drones_quantity', 0.0).get_parameter_value().double_value
        flight_height = self.declare_parameter('flight_height', 0.0).get_parameter_value().double_value
        self.srv = self.create_service(AdvService, 'adv_service', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        global service_active, drones, i, wps_metadata

        response.response = request.tof + request.speed
        self.get_logger().info('Incoming request\ndrone_id: %s speed: %d tof: %d ancho_de_barrido: %d\ncoordx: %d, coordy: %d' % (request.drone_id, \
                        request.speed, request.tof, request.ancho_de_barrido, request.coordx, request.coordy))
        
        drones.append([request.coordx, request.coordy, request.ancho_de_barrido, request.speed, request.tof])
        wps_metadata.add_drone(request.drone_id, request.ancho_de_barrido)

        i = i-1
        if i == 0:
            service_active = False
        return response

"""
class MinimalClient(Node):

    def __init__(self, drone_id, waypoints):
        super().__init__('minimal_client')
        self.client = self.create_client(Waypoints, f'{drone_id}_service')
        self.waypoints = waypoints
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Waypoints.Request()

    def send_request(self):
        #np_array = np.array([[1.0, 2.0, 3.0, 4.0], [21.0, 3.0, 4.0, 5.0]], dtype=float)
        np_array = self.waypoints
        self.req.wps = np_array.flatten().tolist()
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
"""
class MinimalPublisher(Node):

    def __init__(self, drone_id, waypoints):
        super().__init__('minimal_publisher')
        #self.get_logger().info(f'data received {waypoints}')
        self.publisher_ = self.create_publisher(Waypoints, f'{drone_id}_wps', 10)
        self.waypoints = waypoints
        self.drone_id = drone_id
        self.public_wps()

    def public_wps(self):
        msg = Waypoints()
        np_array = self.waypoints
        msg.wps = np_array.flatten().tolist()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % self.drone_id)

def main():
    rclpy.init()

    minimal_service = MinimalService()

    while service_active:
        rclpy.spin_once(minimal_service)

    wps = verdugo(drones, os.path.join(os.getcwd(), 'install/planificador/share/planificador/config/perimeter.yaml'))
    print(drones)

    minimal_service.destroy_node()

    index = 0
    print("waypoints")
    print(wps)

    global flight_height

    drones_names = wps_metadata.flatten()
    proccesed_wps = process_wps(wps, flight_height)

    for list_array_2d in proccesed_wps:
        for array_2d in list_array_2d:
            minimal_publisher = MinimalPublisher(drones_names[index], array_2d)
            minimal_publisher.destroy_node()
            index = index + 1

    rclpy.shutdown()

if __name__ == '__main__':
    main()