import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class Simulation_Results(Node):
    def __init__(self):
        super().__init__('Simulation_Results')

        self.publisher_time= self.create_subscription(Float64, '/execution_time', self.get_exec_time, 10) 

    def get_exec_time(self, msg):
        self.get_logger().info("Received exec time: %f "% msg.data)
        with open("/home/gondolior/Downloads/exec_time", "w") as fin:
            fin.write(f"Execution time was: {msg.data}")

def main():
    rclpy.init()

    simulation_results = Simulation_Results()

    rclpy.spin(simulation_results)

    rclpy.shutdown()

if __name__ == '__main__':
    main()