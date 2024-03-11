import rclpy
from rclpy.node import Node
from syst_msgs.srv import AdvService

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AdvService, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AdvService.Request()

    def send_request(self):
        self.req.drone_id = "my_drone"
        self.req.speed = 12.3
        self.req.tof = 50.2
        self.req.ancho_de_barrido = 33.0
        self.req.coordx = -200.0
        self.req.coordy = 0.0
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request()
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (12.3, 50.2, response.response))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()