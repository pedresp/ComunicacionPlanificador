import rclpy
from rclpy.node import Node
from geometry_msgs.msg._pose_stamped import PoseStamped

from rclpy.executors import MultiThreadedExecutor
from syst_msgs.msg import DronesList

import os, pwd

class Listener_Manager(Node):
    def __init__(self):
        super().__init__('listener_manager')

        self.subscriber_ = self.create_subscription(DronesList, '/droneslist', self.spawn_listeners, 10)

        rclpy.get_default_context().on_shutdown(self.close_file)

    def spawn_listeners(self, msg):
        self.get_logger().info("spawn activated !!!!!")
        mt_executor = MultiThreadedExecutor()
        tlist = []
        m = msg.droneslist
        for i in m:
            self.get_logger().info(f'DRONE {i} will spawn')

        for dn in m:
            self.get_logger().info(f'spawnning drone {dn} of a total of {len(m)}')
            tl = Trajectory_Listener(dn)
            tlist.append(tl)
            mt_executor.add_node(tl)
        
        self.get_logger().info("NOW SPINNING")
        try:
            mt_executor.spin()
            mt_executor.shutdown()
        except KeyboardInterrupt:
            pass
        finally:
            for tl in tlist:
                tl.close_file()
                tl.destroy_node()
            mt_executor.shutdown()

    def close_file(self):
        self.get_logger().info('CERRANDO ARCHIVOOOOOOOOOOOOOOOOOOOO')
        #if not self.file.closed:
        #    self.get_logger().info('ACHIVOOOOOOO CERRADO')
        #    self.file.close()

    def write_coord(self, msg):
        self.get_logger().info("Activado callback")

        self.file.write(f'{msg.pose.position.x},{msg.pose.position.y},{msg.pose.position.z}\n')

class Trajectory_Listener(Node):
    def __init__(self, drone_id):
        super().__init__('trajectory_listener', namespace=drone_id)

        self.drone_name = drone_id
        self.print_when_reach = 10
        self.steps = self.print_when_reach

        self.subscriber_ = self.create_subscription(PoseStamped, f'/{drone_id}/pose', self.write_coord, 10)
        self.file = open(f'/home/{pwd.getpwuid(os.getuid()).pw_name}/sim_stats/{drone_id}-poses.csv', 'w')

        rclpy.get_default_context().on_shutdown(self.close_file)
    
    def close_file(self):
        self.get_logger().info(f"Closed {self.drone_name}'s file")
        if not self.file.closed:
            self.file.close()
    
    def write_coord(self, msg):
        if self.steps == self.print_when_reach:
            self.file.write(f'{msg.pose.position.x},{msg.pose.position.y},{msg.pose.position.z}\n')
            self.steps = 0
        self.steps += 1

def main():
    rclpy.init()
    lm = Listener_Manager()
    try:
        rclpy.spin(lm)
    except KeyboardInterrupt:
        lm.close_file() 
    finally:
        lm.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

