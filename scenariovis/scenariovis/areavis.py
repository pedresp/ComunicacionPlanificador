import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

import yaml
import os, pwd
import numpy as np

class AreaVis(Node):
    def __init__(self):
        super().__init__('areavis')
        
        self.area_publisher = self.create_publisher(Marker, '/area_info', 10) #topic where lines are going to be send
        self.timer_ = self.create_timer(2.0, self.publish_line)

        self.wps  = {} #vertex of the area 
        with open(f'/home/{pwd.getpwuid(os.getuid()).pw_name}/sim_stats/area.yaml', 'r') as y:
            self.wps = yaml.safe_load(y)['areas'][0]['area']['coords']
        
        #self.get_logger().info('%d', self.wps)

        self.vertex_quantity = len(self.wps)
        self.identity = 0 #attribute to generate different ids for each line


    def publish_line(self):
        if self.identity < self.vertex_quantity:
            self.get_logger().info('Timer called')
            next = (self.identity+1)%self.vertex_quantity

            self.get_logger().info("%d %d" % (self.identity, next))
            marker = Marker()

            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()

            marker.ns = "areavis"
            marker.id = self.identity
            marker.type = Marker.CYLINDER
            marker.action = Marker.ADD

            marker.color.r = 0.0
            marker.color.g = 0.0
            marker.color.b = 0.0
            marker.color.a = 1.0

            current_point = np.array([self.wps[self.identity]['x'], self.wps[self.identity]['y'], 0.0])
            next_point = np.array([self.wps[next]['x'], self.wps[next]['y'], 0.0])

            middle_point = (current_point + next_point) / 2.0 #calculate center of the cylinder
            points_vector = next_point - current_point #vector determined by current-next points

            pv_module = np.linalg.norm(points_vector) #calculate point_vector module == distance between current-next points 
            norm_pv = points_vector / pv_module #normalize pv vector

            axis_z = np.array([0.0, 0.0, 1.0])
            rotation_axis = np.cross(axis_z, norm_pv)
            if np.linalg.norm(rotation_axis) == 0:
                quaternion = np.array([1.0, 0.0, 0.0, 0.0]) #quaternion describing the turn (w,x,y,z)
            else:
                norm_rotation_axis = rotation_axis/ np.linalg.norm(rotation_axis)
                zpv_angle = np.arccos(np.dot(axis_z, norm_pv)) #angle between z axis an points vector
                #calculate quaternion of the turn
                quaternion = np.concatenate(([np.cos(zpv_angle / 2.0)], norm_rotation_axis * np.sin(zpv_angle / 2.0)))

            marker.pose.position.x = middle_point[0]
            marker.pose.position.y = middle_point[1]
            marker.pose.position.z = middle_point[2]

            marker.pose.orientation.w = quaternion[0]
            marker.pose.orientation.x = quaternion[1]
            marker.pose.orientation.y = quaternion[2]
            marker.pose.orientation.z = quaternion[3]

            marker.scale.x = 0.5
            marker.scale.y = 0.5
            marker.scale.z = pv_module

            self.area_publisher.publish(marker)
            self.identity += 1 

def main():
    rclpy.init()
    areavis = AreaVis()
    try:
        rclpy.spin(areavis)
    except KeyboardInterrupt:
        pass
    finally:
        areavis.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
