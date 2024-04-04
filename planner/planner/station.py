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

class Station(Node):

    def __init__(self):
        super().__init__('Station')
        
        global i, flight_height
        i = self.declare_parameter('drones_quantity', 0.0).get_parameter_value().double_value
        flight_height = self.declare_parameter('flight_height', 0.0).get_parameter_value().double_value
        self.srv = self.create_service(AdvService, '/adv_service', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        global service_active, drones, i, wps_metadata
        
        if service_active:
            response.response = 1.0
            self.get_logger().info('Incoming request\ndrone_id: %s speed: %d tof: %d ancho_de_barrido: %d\ncoordx: %d, coordy: %d' % (request.drone_id, \
                            request.speed, request.tof, request.ancho_de_barrido, request.coordx, request.coordy))
            
            drones.append([request.coordx, request.coordy, request.ancho_de_barrido, request.speed, request.tof])
            wps_metadata.add_drone(Drone_initial(request.drone_id, (request.coordx, request.coordy)), request.ancho_de_barrido)

            i = i-1
            if i == 0:
                service_active = False
                self.publish_wps()
            return response
        response.response = 0.0
        return response
    
    def publish_wps(self):
        global drones, wps_metadata, flight_height
        wps = verdugo(drones, os.path.join(os.getcwd(), 'install/planner/share/planner/config/perimeter.yaml'))

        index = 0

        drones_names = wps_metadata.flatten()
        proccesed_wps = process_wps(wps, flight_height)

        for list_array_2d in proccesed_wps:
            for array_2d in list_array_2d:
                array_to_send = np.append(np.array([[drones_names[index].coords[0], drones_names[index].coords[1], flight_height]]), \
                                      array_2d, axis=0)
                publisher = self.create_publisher(Waypoints, f'/{drones_names[index].name}/route', 10)
                msg = Waypoints()
                msg.wps = array_to_send.flatten().tolist()

                publisher.publish(msg)
                self.get_logger().info('Publishing: "%s"' % drones_names[index])
                index = index + 1

def main():
    rclpy.init()

    station = Station()

    rclpy.spin(station)

    rclpy.shutdown()

if __name__ == '__main__':
    main()