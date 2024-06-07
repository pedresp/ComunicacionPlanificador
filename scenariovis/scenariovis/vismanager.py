import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

from .auxiliar import readCSV
from .BST import BST
import os, pwd, time
import threading

route = f'/home/{pwd.getpwuid(os.getuid()).pw_name}/sim_stats/'

def spin_printtray(planned_node):
    planned_node.publish_route()
    planned_node.destroy_node()

class Vismanager(Node):
    def __init__(self):
        super().__init__('vismanager')
        self.pps = {} #map containing all planned paths

        #self.mthreaded_planned = MultiThreadedExecutor()
        self.planned_threads = []
        self.real_threads = []

        bst = None 
        ppf = [file for file in os.listdir(f'{route}') if file.endswith('-planned.csv')] #lst of files containing planned paths
        for file in ppf:
            path = readCSV(f'{route}{file}')#read path coordinates
            name = file.split('-planned.csv')[0]

            bst = BST.add_node(bst, BST(path[1][1], name))
            ppn = Planned_Path(name, path) 

            #self.mthreaded_planned.add_node(ppn)
            self.planned_threads.append(threading.Thread(target=spin_printtray, args=(ppn,))) 
            self.planned_threads[-1].start() 
        
        for file in bst.get_names():
            path = readCSV(f'{route}{file}-poses.csv')

            rpn = Real_Path(file, path, (0.0, 1.0, 0.0))
            self.real_threads.append(threading.Thread(target=spin_printtray, args=(rpn,)))
            self.real_threads[-1].start()

        for thread in self.planned_threads:
            thread.join()
        for thread in self.real_threads:
            thread.join()
        self.get_logger().info("JOINED THREADS")
        #self.mthreaded_planned.spin()
        #self.mthreaded_planned.shutdown()


class Planned_Path(Node):
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
            marker.type = Marker.LINE_STRIP
            marker.action = Marker.ADD

            marker.color.r = 1.0
            marker.color.g = 0.0
            marker.color.b = 1.0
            marker.color.a = 1.0

            marker.scale.x = 1.0 
            marker.scale.y = 1.0
            marker.scale.z = 1.0

            p = Point()
            q = Point()

            p.x = self.path[self.index][0]
            p.y = self.path[self.index][1]
            p.z = 0.0
            q.x = self.path[next][0]
            q.y = self.path[next][1]
            q.z = 0.0

            marker.points.append(p)
            marker.points.append(q)

            self.pp_publisher.publish(marker)
            self.index += 1 

class Real_Path(Node):
    def __init__(self, drone_id, path, color):
        super().__init__('real_path', namespace=drone_id)

        self.drone_id = drone_id
        self.path = path
        self.color = color

        self.rp_publisher = self.create_publisher(Marker, 'realpath', 400)

        self.point_quantity = len(path)
        self.index = 0

    def publish_route(self):
        for i in range(self.point_quantity):
            time.sleep(0.1)
            self.publish_line()

    def publish_line(self):
        if self.index < self.point_quantity - 1:
            next = self.index + 1
            marker = Marker() 

            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()

            marker.ns = f"{self.drone_id}@realpath"
            marker.id = self.index
            marker.type = Marker.LINE_STRIP
            marker.action = Marker.ADD

            marker.color.r = self.color[0] 
            marker.color.g = self.color[1]
            marker.color.b = self.color[2]
            marker.color.a = 1.0

            marker.scale.x = 1.0
            marker.scale.y = 1.0
            marker.scale.z = 1.0

            p = Point()
            q = Point()

            p.x = self.path[self.index][0]
            p.y = self.path[self.index][1]
            p.z = self.path[self.index][2]
            q.x = self.path[next][0]
            q.y = self.path[next][1]
            q.z = self.path[self.index][2]

            marker.points.append(p)
            marker.points.append(q)

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