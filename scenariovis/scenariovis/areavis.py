import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

import yaml
import os, pwd

class AreaVis(Node):
    def __init__(self):
        super().__init__('areavis')
        
        self.area_publisher = self.create_publisher(Marker, '/area_info', 10) #topic where lines are going to be send
        self.timer_ = self.create_timer(1.3, self.publish_line)

        self.wps  = {} #vertex of the area 
        with open(f'/home/{pwd.getpwuid(os.getuid()).pw_name}/sim_stats/area.yaml', 'r') as y:
            self.wps = yaml.safe_load(y)['areas'][0]['area']['coords']
        
        #self.get_logger().info('%d', self.wps)

        self.vertex_quantity = len(self.wps)
        self.identity = 0 #attribute to generate different ids for each line


    def publish_line(self):
        self.get_logger().info('Timer called')
        if self.identity < self.vertex_quantity - 1: 
            marker = Marker()

            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()

            marker.ns = "areavis"
            marker.id = self.identity
            marker.type = Marker.LINE_STRIP
            marker.action = Marker.ADD

            marker.color.r = 0.0
            marker.color.g = 0.0
            marker.color.b = 0.0
            marker.color.a = 0.0

            marker.scale.x = 0.5

            p = Point()
            q = Point()

            p.x = self.wps[self.identity]['x']
            p.y = self.wps[self.identity]['y']
            p.z = 0.0
            q.x = self.wps[self.identity+1]['x']
            q.y = self.wps[self.identity+1]['y']
            q.z = 0.0

            marker.points.append(p)
            marker.points.append(p)

            self.area_publisher.publish(marker)
            self.identity += 1 

def main():
    rclpy.init()
    areavis = AreaVis()
    rclpy.spin(areavis)
    rclpy.shutdown()

if __name__ == '__main__':
    main()