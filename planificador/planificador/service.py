from syst_msgs.srv import AdvService
import rclpy
from rclpy.node import Node

from planning_algorithm.main import verdugo

i = 3
service_active = True
drones = []

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AdvService, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        global service_active, drones, i

        response.response = request.tof + request.speed
        self.get_logger().info('Incoming request\ndrone_id: %s speed: %d tof: %d ancho_de_barrido: %d\ncoordx: %d, coordy: %d' % (request.drone_id, \
                        request.speed, request.tof, request.ancho_de_barrido, request.coordx, request.coordy))
        
        drones.append([request.coordx, request.coordy, request.ancho_de_barrido, request.speed, request.tof])

        i = i-1
        if i == 0:
            service_active = False
        return response

def main():
    rclpy.init()

    minimal_service = MinimalService()

    while service_active:
        rclpy.spin_once(minimal_service)

    verdugo(drones)

    print(drones)
    rclpy.shutdown()

if __name__ == '__main__':
    main()