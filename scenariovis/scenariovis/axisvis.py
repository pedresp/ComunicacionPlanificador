import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

import yaml
import os, pwd, time
import numpy as np

class AxisVis(Node):
    def __init__(self):
        super().__init__('axisvis')
        
        self.x= self.create_publisher(Marker, 'xview', 30) #topic where lines are going to be send
        self.ident= 0
#        self.timer_ = self.create_timer(1.0, self.publish_line)

        for j in range(-250, 250, 25):
            i = float(j)
            self.publish_line(self.ident, [i, 0.0, 0.0], [i+25.0,0.0,0.0])        
            self.publish_text(self.ident+1, [i+25, 0.0, 0.,0], str(i+25))
            self.ident += 2 

        for j in range(-250,250,25):
            i = float(j)
            self.publish_line(self.ident, [0.0, i, 0.0], [0.0, i+25.0, 0.0])
        #self.get_logger().info('%d', self.wps)
            self.publish_text(self.ident+1, [0.0, i+25, 0.0], str(i+25))
            self.ident += 2 

        for j in range(0, 25, 5):
            i = float(j)
            self.publish_line(self.ident, [0.0,0.0,i], [0.0,0.0,i+5.0])
            self.publish_text(self.ident+1, [0.0, 0.0, i+5], str(i+5))
            self.ident += 2

    def publish_text(self, i, position, text):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "texto"
        marker.id = int(i)
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD
        marker.scale.z = 2.0

        marker.scale.x = 2.0
        marker.scale.y = 2.0

        marker.pose.position.x = 5.0 if position[1] == 0 and position[0] == 0 else position[0]
        marker.pose.position.y = position[1]
        marker.pose.position.z = 5.0 if position[2] == 0 else position[2]

        marker.text = text
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        self.x.publish(marker)
    def publish_line(self, i, wps, pwps):
        time.sleep(0.5)
        self.get_logger().info('Timer called')

        marker = Marker()

        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()

        marker.ns = "axis"
        marker.id = int(i)
        marker.type = Marker.CYLINDER
        marker.action = Marker.ADD
        marker.text = str(i)

        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        current_point = np.array(wps)
        next_point = np.array(pwps)

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

        marker.scale.x = 0.3
        marker.scale.y = 0.3
        marker.scale.z = pv_module

        self.x.publish(marker)

def main():
    rclpy.init()
    areavis = AxisVis()
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
