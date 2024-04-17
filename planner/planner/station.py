from syst_msgs.srv import AdvService
from syst_msgs.msg import Waypoints
import rclpy
from rclpy.node import Node

from planning_algorithm.main import planning_algorithm
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
        self.srv = self.create_service(AdvService, '/advertisement_service', self.register_drone)

    def register_drone(self, request, response):
        global service_active, drones, i, wps_metadata
        
        if service_active:
            response.response = 1.0
            self.get_logger().info('Incoming request\ndrone_id: %s speed: %d tof: %d sweep_width: %d\ncoordx: %d, coordy: %d' % (request.drone_id, \
                            request.speed, request.tof, request.sweep_width, request.coordx, request.coordy))
            
            drones.append([request.coordx, request.coordy, request.sweep_width, request.speed, request.tof])
            wps_metadata.add_drone(Drone_initial(request.drone_id, (request.coordx, request.coordy)), request.sweep_width)

            i = i-1
            if i == 0:
                service_active = False
                self.publish_wps()
            return response
        response.response = 0.0
        return response
    
    def publish_wps(self):
        global drones, wps_metadata, flight_height
        wps = planning_algorithm(drones, os.path.join(os.getcwd(), 'install/planner/share/planner/config/perimeter.yaml'), wps_metadata.flatten_str())

        index = 0

        drones_names = wps_metadata.flatten()
        proccesed_wps = process_wps(wps, flight_height)

        for list_array_2d in proccesed_wps:
            for array_2d in list_array_2d:
                array_to_send = np.append(np.array([[drones_names[index].coords[0], drones_names[index].coords[1], 0]]), \
                                    array_2d, axis=0)
                array_to_send = np.append(array_to_send, np.array([[drones_names[index].coords[0], \
                                    drones_names[index].coords[1], 0]]), axis=0)
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