import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

from sim_msgs.msg import DroneResults

exec_time = -1.0

class Simulation_Results(Node):
    def __init__(self):
        super().__init__('Simulation_Results')

        self.drones_quantity = self.declare_parameter('drones_quantity', 0.0).get_parameter_value().double_value
        self.drones_received = []
        
        self.publisher_time= self.create_subscription(Float64, '/execution_time', self.get_exec_time, 10) 
        self.subscriber_drones_result= self.create_subscription(DroneResults, '/drone_results', self.receive_drone_result, 10)

    def get_exec_time(self, msg):
        global exec_time

        exec_time = msg.data
        self.get_logger().info("Received exec time: %f "% msg.data)
        #with open("/home/gondolior/Downloads/exec_time", "w") as fin:
        #    fin.write(f"Execution time was: {msg.data}")

    def receive_drone_result(self, msg):
        self.get_logger().info("Received drone: %s" % msg.drone_id)

        self.drones_received.append((msg.drone_id, msg.total_time, msg.total_distance))
        self.drones_quantity -= 1

        if self.drones_quantity == 0:
            with open("/home/gondolior/Downloads/exec_time", "w") as fin:
              fin.write(f"Execution time was: {exec_time}\n") 
              for elem in self.drones_received:
                  fin.write(f"{elem[0]} -> TT: {elem[1]} -> TD: {elem[2]}\n")

def main():
    rclpy.init()

    simulation_results = Simulation_Results()

    rclpy.spin(simulation_results)

    rclpy.shutdown()

if __name__ == '__main__':
    main()