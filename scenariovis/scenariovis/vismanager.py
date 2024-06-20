import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

from .auxiliar import readCSV
from .BST import BST
import os, pwd, time
import threading

import numpy as np

route = f'/home/{pwd.getpwuid(os.getuid()).pw_name}/sim_stats/'

def spin_printtray(planned_node):
    planned_node.publish_route()
    planned_node.destroy_node()

class Vismanager(Node):
    def __init__(self):
        super().__init__('vismanager')
        self.pps = {} #map containing all planned paths

        time.sleep(2)
        #self.mthreaded_planned = MultiThreadedExecutor()
        self.planned_threads = []
        self.real_threads = []

        self.colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 1.0), (0.0, 1.0, 0.0), (1.0, 0.0, 1.0), (0.0, 0.0, 1.0), (1.0, 1.0, 0.0)]

        bst = None 
        ppf = [file for file in os.listdir(f'{route}') if file.endswith('-planned.csv')] #lst of files containing planned paths
        for file in ppf:
            path = readCSV(f'{route}{file}')#read path coordinates
            name = file.split('-planned.csv')[0]

            bst = BST.add_node(bst, BST(path[1][1], name))
            ppn = PP_Publisher(name, path) 

            #self.mthreaded_planned.add_node(ppn)
            self.planned_threads.append(threading.Thread(target=spin_printtray, args=(ppn,))) 
            self.planned_threads[-1].start() 
        
        i = 0
        for file in bst.get_names():
            path = readCSV(f'{route}{file}-poses.csv')

            rpn = RP_Publisher(file, path, self.colors[i])
            self.real_threads.append(threading.Thread(target=spin_printtray, args=(rpn,)))
            self.real_threads[-1].start()

            i = (i+1)%6

        for thread in self.planned_threads:
            thread.join()
        for thread in self.real_threads:
            thread.join()
        self.get_logger().info("JOINED THREADS")
        #self.mthreaded_planned.spin()
        #self.mthreaded_planned.shutdown()


class PP_Publisher(Node):
    def __init__(self, drone_id, path):
        super().__init__('planned_path', namespace=drone_id) 

        self.drone_id = drone_id
        self.path = path

        self.pp_publisher = self.create_publisher(Marker, 'plannedpath', 10)
        #self.timer_ = self.create_timer(1.0, self.publish_line)

        self.point_quantity = len(self.path)
        self.index = 0

    def publish_route(self):
        for i in range(self.point_quantity):
            time.sleep(0.5)
            self.publish_line()

    def publish_line(self):
        if self.index < self.point_quantity - 1:
            next = self.index + 1
            marker = Marker() 

            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()

            marker.ns = f"{self.drone_id}@plannedpath"
            marker.id = self.index
            marker.type = Marker.CYLINDER
            marker.action = Marker.ADD

            marker.color.r = 0.196
            marker.color.g = 0.329
            marker.color.b = 0.243
            marker.color.a = 0.8

            current_point = np.array([self.path[self.index][0], self.path[self.index][1], 0.0])
            next_point = np.array([self.path[next][0], self.path[next][1], 0.0])

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

            self.pp_publisher.publish(marker)
            self.index += 1 

class RP_Publisher(Node):
    def __init__(self, drone_id, path, color):
        super().__init__('real_path', namespace=drone_id)

        self.drone_id = drone_id
        self.path = path
        self.color = color

        self.rp_publisher = self.create_publisher(Marker, 'realpath', 600)

        self.point_quantity = len(path)
        self.index = 0

    def publish_route(self):
        for i in range(self.point_quantity):
            time.sleep(0.1)
            self.publish_line()

        self.get_logger().info("PUBLISHED: %s" % self.point_quantity)

    def publish_line(self):
        if self.index < self.point_quantity - 1:
            next = self.index + 1
            marker = Marker() 

            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()

            marker.ns = f"{self.drone_id}@realpath"
            marker.id = self.index
            marker.type = Marker.CYLINDER
            marker.action = Marker.ADD

            current_point = np.array([self.path[self.index][0], self.path[self.index][1], self.path[self.index][2]])
            next_point = np.array([self.path[next][0], self.path[next][1], self.path[next][2]])

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

            marker.color.r = self.color[0] 
            marker.color.g = self.color[1]
            marker.color.b = self.color[2]
            marker.color.a = 1.0


            self.rp_publisher.publish(marker)
            self.index += 1 

def main():
    rclpy.init()
    vm = Vismanager()
    try:
        rclpy.spin(vm)
    except KeyboardInterrupt:
        pass
    finally:
        vm.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
