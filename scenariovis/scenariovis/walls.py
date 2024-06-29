import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

import time

class W_Plane(Node):
    def __init__(self):
        super().__init__('walls')
        self.plane_publisher = self.create_publisher(Marker, 'walls', 10)
        self.get_logger().info('PREPARING WALL')
        time.sleep(3)
        self.publish_walls(0, [-27.5, 200.1, 50.0], [345.0, 0.01, 100.0])
        self.publish_walls(1, [145.1, 50.0, 50.0], [0.01, 300.0, 100.0])

    def publish_walls(self, wid, posit, wide):
        # Crear el marcador de plano
        plane_marker = Marker()
        plane_marker.header.frame_id = "map"
        plane_marker.header.stamp = self.get_clock().now().to_msg()
        plane_marker.ns = "walls"
        plane_marker.id = wid
        plane_marker.type = Marker.CUBE
        plane_marker.action = Marker.ADD
        plane_marker.pose.position.x = posit[0]
        plane_marker.pose.position.y = posit[1]
        plane_marker.pose.position.z = posit[2]
        plane_marker.pose.orientation.x = 0.0
        plane_marker.pose.orientation.y = 0.0
        plane_marker.pose.orientation.z = 0.0
        plane_marker.pose.orientation.w = 1.0
        plane_marker.scale.x = wide[0] # Ancho del plano
        plane_marker.scale.y = wide[1]  # Altura del plano
        plane_marker.scale.z = wide[2]  # Grosor del plano
        plane_marker.color.r = 1.0  # Componente rojo
        plane_marker.color.g = 1.0  # Componente verde
        plane_marker.color.b = 1.0  # Componente azul
        plane_marker.color.a = 1.0  # Opacidad (0.5 es semi-opaco)

        self.plane_publisher.publish(plane_marker)

        # Crear el marcador de cuadrícula
#        grid_marker = Marker()
#        grid_marker.header.frame_id = "map"
#        grid_marker.header.stamp = self.get_clock().now().to_msg()
#        grid_marker.ns = "grid"
#        grid_marker.id = 1
#        grid_marker.type = Marker.LINE_LIST
#        grid_marker.action = Marker.ADD
#        grid_marker.scale.x = 0.1  # Grosor de las líneas de la cuadrícula
#        grid_marker.scale.y = 0.1  
#        grid_marker.scale.z = 0.1  
#        grid_marker.color.r = 0.0
#        grid_marker.color.g = 0.0
#        grid_marker.color.b = 0.0
#        grid_marker.color.a = 1.0  # Opacidad total
#
#        grid_size = 30.0  # Tamaño de la cuadrícula
#        step = 5.0  # Espaciado entre las líneas de la cuadrícula
#
#        # Crear las líneas de la cuadrícula
#        for i in range(int(grid_size / step) + 1):
#            # Líneas verticales
#            start_point = Point()
#            end_point = Point()
#            start_point.x = -grid_size / 2 + i * step
#            start_point.y = 0.0
#            start_point.z = -grid_size / 2
#            end_point.x = -grid_size / 2 + i * step
#            end_point.y = 0.0
#            end_point.z = grid_size / 2
#            grid_marker.points.append(start_point)
#            grid_marker.points.append(end_point)
#
#            # Líneas horizontales
#            start_point = Point()
#            end_point = Point()
#            start_point.x = -grid_size / 2
#            start_point.y = 0.0
#            start_point.z = -grid_size / 2 + i * step
#            end_point.x = grid_size / 2
#            end_point.y = 0.0
#            end_point.z = -grid_size / 2 + i * step
#            grid_marker.points.append(start_point)
#            grid_marker.points.append(end_point)
#
#        self.publisher_.publish(grid_marker)

def main(args=None):
    rclpy.init(args=args)
    walls = W_Plane()
    rclpy.spin(walls)
    walls.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

