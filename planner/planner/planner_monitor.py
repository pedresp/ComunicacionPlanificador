import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

from sim_msgs.msg import DroneResults

import pwd, os
exec_time = -1.0

class Planner_Monitor(Node):
    def __init__(self):
        super().__init__('Planner_Monitor')

        self.drones_quantity = self.declare_parameter('drones_quantity', 0.0).get_parameter_value().double_value
        self.drones_received = []
        
        self.publisher_time= self.create_subscription(Float64, '/execution_time', self.get_exec_time, 10) 
        self.subscriber_drones_result= self.create_subscription(DroneResults, '/drone_results', self.receive_drone_result, 10)

    def get_exec_time(self, msg):
        global exec_time

        exec_time = msg.data
        self.get_logger().info("Received exec time: %f "% msg.data)

    def receive_drone_result(self, msg):
        self.get_logger().info("Received drone: %s" % msg.drone_id)

        self.drones_received.append((msg.drone_id, msg.total_time, msg.total_distance))
        self.drones_quantity -= 1

        if self.drones_quantity == 0:
            with open(f"/home/{pwd.getpwuid(os.getuid()).pw_name}/sim_stats/after_simulation_metrics.csv", "w") as fin:
              fin.write(f"algorithm_execution_time,{exec_time}\n\nUAV,Total time,Total distance\n") 
              for elem in self.drones_received:
                  fin.write(f"{elem[0]},{elem[1]},{elem[2]}\n")

def main():
    rclpy.init()

    planner_monitor= Planner_Monitor()

    rclpy.spin(planner_monitor)

    rclpy.shutdown()

if __name__ == '__main__':
    main()