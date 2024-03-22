from sim_msgs.msg import Waypoints
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker
import rclpy
from rclpy.node import Node
import time
import random

class WpSubscriber(Node):
    def __init__(self):
        super().__init__('vis_listener')
        
        self.subscription = self.create_subscription(Waypoints,'wps',self.visualize,1)
        self.subscription

    def visualize(self,msg):
        pose_publisher = MarkerPublisher(msg.wps)
        rclpy.spin(pose_publisher)

class MarkerPublisher(Node):
    def __init__(self, wps):
        super().__init__('wp_vis')

        self.publisher_ = self.create_publisher(Marker, 'marker', 100)

        i = 0
        before = None
        
        red = random.random()
        blue = random.random()
        green = random.random()

        for wp in wps:
            m = Marker()
            m.ns = "wp_vis"
            m.header.frame_id = "base_link"
            m.type = Marker.SPHERE
            m.action = Marker.ADD
            m.scale.x = 1.5
            m.scale.y = 1.5
            m.scale.z = 1.5
            m.color.a = 1.0
            m.color.r = 1.0
            m.id = i

            if before != None:
                i = i + 1
                l = Marker()
                l.ns = "wp_vis"
                l.header.frame_id = "base_link"
                l.type = Marker.LINE_STRIP
                l.action = Marker.ADD
                l.scale.x = 0.5
                l.color.a = 1.0
                l.color.r = red
                l.color.b = blue
                l.color.g = green
                l.id = i
                points = []
                pointA = Point()
                pointB = Point()
                pointA.x = before.pose.position.x
                pointA.y = before.pose.position.y
                pointA.z = before.pose.position.z
                pointB.x = wp.pose.position.x
                pointB.y = wp.pose.position.y
                pointB.z = wp.pose.position.z
                points.append(pointA)
                points.append(pointB)
                l.points = points
                # time.sleep(0.1)
                self.publisher_.publish(l)


            m.pose.position.x = wp.pose.position.x
            m.pose.position.y = wp.pose.position.y
            m.pose.position.z = wp.pose.position.z

            time.sleep(0.05)
    
            self.publisher_.publish(m)

            before = wp
            i = i + 1

def main():
    rclpy.init()
    pose_subscriber = WpSubscriber()
    rclpy.spin(pose_subscriber)
