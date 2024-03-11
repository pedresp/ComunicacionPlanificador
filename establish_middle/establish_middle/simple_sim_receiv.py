import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalListener(Node):

    def __init__(self):
        super().__init__('minimal_listener')
        self.publisher_ = self.create_publisher(String, 'establish', 10)
        self.listener_ = self.create_subscription(String, 'establish', self.listener_callback, 10)
        self.i = 0


    def listener_callback(self, msg):
        self.get_logger().info('I received %s' % msg.data)
        msg2 = String()
        msg2.data = 'Hi'
        if msg.data != 'Hi':
            self.publisher_.publish(msg2)


def main(args=None):
    rclpy.init(args=args)

    minimal_listener = MinimalListener()

    rclpy.spin(minimal_listener)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()