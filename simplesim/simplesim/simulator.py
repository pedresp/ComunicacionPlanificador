from .random_waypoints_generator import *

from sim_msgs.msg import Waypoints
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Vector3
from nav_msgs.msg import Path
import rclpy
from rclpy.node import Node
import math
import time

MAX_SPEED = float(20) # m/s
MAX_ACCELERATION = float(40) # m/s²
TIME_STEP = 0.1 # s
TIME_SPENT = 0.0
NEAR_POINT = float(15) # m. Distance to which a drone is
               # considered near a point.
IN_POINT = 7
MIN_ARC_RADIUS = 10 # m

current_direction = Vector3()
current_speed = float(0) #m/s
path = []

class Publisher(Node):
    def __init__(self, wps):

        global MAX_SPEED
        global MAX_ACCELERATION
        global DRONE_ID

        super().__init__('simulator')

        self.publisher_ = self.create_publisher(PoseStamped, 'pose', 1)

        MAX_SPEED = self.declare_parameter(
            'max_speed', 20.0).get_parameter_value().double_value

        MAX_ACCELERATION = self.declare_parameter(
            'max_acc', 40.0).get_parameter_value().double_value
        
        DRONE_ID = self.declare_parameter(
            'drone_id', 'drone_x').get_parameter_value().string_value

        start(self, wps[0], wps[1:])

class PathPublisher(Node):
    def __init__(self):
        super().__init__('path')

        self.publisher_ = self.create_publisher(Path, 'path', 1)

class Subscriber(Node):
    def __init__(self):
        super().__init__('sim_listener')

        self.subscription = self.create_subscription(Waypoints,'wps', self.startup, 1)
        self.subscription

    def startup(self,msg):
        wps = msg.wps
        pose_publisher = Publisher(wps)
        rclpy.spin(pose_publisher)

def start(publisher, current_wp: PoseStamped, waypoints: list[PoseStamped]):
    """
    Takes in the desired waypoints,
    processes a path in real time and makes
    the drone 'fly' through it in RViz
    using Pose messages
    """
    time.sleep(5)
    # Calculate direction of first waypoint
    current_direction = calculate_direction(current_wp, waypoints[0])

    print_vec(current_direction)

    for next_wp in waypoints[:-1]:
        subsequent = waypoints[waypoints.index(next_wp)+1]
        current_wp = approach(publisher, current_wp, next_wp, subsequent)
        current_wp = overtake(publisher, current_wp, subsequent)
    finish(publisher, current_wp, waypoints[-1]) # Last point
    publisher.get_logger().info(f'TOTAL TIME: {TIME_SPENT:.3f}')

def approach(publisher, current, next_wp, subsequent) -> PoseStamped:
    """
    Approaches next point from
    current point in a straight line
    """
    print("*** APPROACH ***")

    global current_speed
    global current_direction
    global path
    global TIME_SPENT

    current_direction = calculate_direction(current, next_wp)
    curr_time = 0
    previous_speed = current_speed
    near_point = calculate_near_point(calculate_overtake_speed(calculate_angle(current, next_wp, subsequent)), MAX_SPEED)
    publisher.get_logger().info(f'NEAR POINT CALCULATED: {near_point + IN_POINT}')
    publisher.get_logger().info(f'Vf: {calculate_overtake_speed(calculate_angle(current, next_wp, subsequent))} Vi: {MAX_SPEED}')
    while distance(current, next_wp) > IN_POINT:
        if distance(current, next_wp) > near_point+IN_POINT:
            # publisher.get_logger().info("NOT_NEAR")
            current_speed = calculate_speed(MAX_ACCELERATION)
        else:
            if curr_time < 1:
                curr_time += TIME_STEP
            # publisher.get_logger().info("NEAR_POINT")
            angle = calculate_angle(current, next_wp, subsequent)
            # publisher.get_logger().info("ANGLE")
            # publisher.get_logger().info(f'{angle}')
            current_speed = calculate_speed(acceleration_with_goal_speed(lerp(previous_speed, calculate_overtake_speed(angle), curr_time)))
        
        # publisher.get_logger().info("SPEED")
        # publisher.get_logger().info(str(current_speed))
        print("DIRECTION")
        print_vec(current_direction)

        next_pose = PoseStamped()
        next_pose.pose.position.x = current.pose.position.x + current_direction.x * (current_speed*TIME_STEP)
        next_pose.pose.position.y = current.pose.position.y + current_direction.y * (current_speed*TIME_STEP)
        next_pose.pose.position.z = current.pose.position.z + current_direction.z * (current_speed*TIME_STEP)

        print("POSITION")
        print_point(next_pose)
        print("")
        next_pose.header.frame_id = "base_link"

        publisher.publisher_.publish(next_pose)
        path.append(next_pose)
        new_path = Path()
        new_path.header.frame_id = "base_link"
        new_path.poses = path
        # path_publisher.publisher_.publish(new_path)
        current = next_pose

        TIME_SPENT += TIME_STEP
        time.sleep(TIME_STEP)

    return current

def overtake(publisher, current, next_wp) -> PoseStamped:
    """
    Passes near point and redirects
    drone towards next point
    """
    print("*** OVERTAKE ***")

    global current_speed
    global current_direction
    global path
    global TIME_SPENT

    print_point(current)
    print_point(next_wp)

    next_direction = calculate_direction(current, next_wp)

    i = 0
    print_vec(current_direction)
    print_vec(next_direction)
    while i < 1:
        new_current_direction = slerp(current_direction, next_direction, i)
        i = i + TIME_STEP

        print("SPEED")
        print(str(current_speed))
        print("DIRECTION")
        print_vec(new_current_direction)

        next_pose = PoseStamped()
        next_pose.pose.position.x = current.pose.position.x + new_current_direction.x * (current_speed*TIME_STEP)
        next_pose.pose.position.y = current.pose.position.y + new_current_direction.y * (current_speed*TIME_STEP)
        next_pose.pose.position.z = current.pose.position.z + new_current_direction.z * (current_speed*TIME_STEP)

        print("POSITION")
        print_point(next_pose)
        print("")
        next_pose.header.frame_id = "base_link"

        publisher.publisher_.publish(next_pose)
        path.append(next_pose)
        current = next_pose

        TIME_SPENT += TIME_STEP
        time.sleep(TIME_STEP)
    current_direction = new_current_direction
    return current

def finish(publisher, current, next_wp) -> None:
    """
    Goes towards last waypoint.
    Slows speed until it's zero
    """

    print("*** FINISH ***")

    global current_speed
    global current_direction
    global path
    global TIME_SPENT

    current_direction = calculate_direction(current, next_wp)

    while distance(current, next_wp) > 2:
        if distance(current, next_wp) > 2:
            current_speed = calculate_speed(MAX_ACCELERATION)
        else:
            current_speed = calculate_speed(acceleration_with_goal_speed(calculate_overtake_speed(0)))

        print("SPEED")
        print(str(current_speed))
        print("DIRECTION")
        print_vec(current_direction)

        next_pose = PoseStamped()
        next_pose.pose.position.x = current.pose.position.x + current_direction.x * (current_speed*TIME_STEP)
        next_pose.pose.position.y = current.pose.position.y + current_direction.y * (current_speed*TIME_STEP)
        next_pose.pose.position.z = current.pose.position.z + current_direction.z * (current_speed*TIME_STEP)

        print("POSITION")
        print_point(next_pose)
        print("")
        next_pose.header.frame_id = "base_link"

        publisher.publisher_.publish(next_pose)
        path.append(next_pose)
        current = next_pose

        TIME_SPENT += TIME_STEP
        time.sleep(TIME_STEP)

def distance(a: PoseStamped, b: PoseStamped) -> float:
    """
    Calculates distance between two points
    """
    return math.sqrt((b.pose.position.x - a.pose.position.x) ** 2 + (b.pose.position.y - a.pose.position.y) ** 2 + (b.pose.position.z - a.pose.position.z) ** 2)

def calculate_overtake_speed(angle: float) -> float:
    """
    Calculates the speed needed
    to pass through an angle
    """
    return (angle)/(math.pi) * MAX_SPEED

def acceleration_with_goal_speed(goal: float) -> float:
    """
    Calculates acceleration needed for certain speed goal
    """
    a = (goal - current_speed)/TIME_STEP
    if a > MAX_ACCELERATION:
        return MAX_ACCELERATION
    elif a < -MAX_ACCELERATION:
        return -MAX_ACCELERATION
    else:
        return a

def calculate_speed(acceleration: float):
    """
    Calculates speed based on current acceleration
    """
    v = current_speed + acceleration * TIME_STEP
    if v > MAX_SPEED:
        return MAX_SPEED
    elif v < -MAX_SPEED:
        return -MAX_SPEED
    else:
        return v

def calculate_angle(point_x, point_y, point_z) -> float:
    """
    Calculates angle between three waypoints
    in radians
    """
    # calculate A (X->Y) and B (Y->Z) vectors
    a_x = point_x.pose.position.x - point_y.pose.position.x
    a_y = point_x.pose.position.y - point_y.pose.position.y
    a_z = point_x.pose.position.z - point_y.pose.position.z

    b_x =  point_z.pose.position.x - point_y.pose.position.x
    b_y =  point_z.pose.position.y - point_y.pose.position.y
    b_z =  point_z.pose.position.z - point_y.pose.position.z

    # dot product
    dot_product = a_x * b_x + a_y * b_y + a_z * b_z
    print(f"dot product: {dot_product}")
    # magnitudes
    mag_a = math.sqrt(a_x**2 + a_y**2 + a_z**2)
    print(f"mag a: {mag_a}")
    mag_b = math.sqrt(b_x**2 + b_y**2 + b_z**2)
    print(f"mag b: {mag_b}")

    x = dot_product/(mag_a*mag_b)
    if x > 1: # evita errores de dominio por la coma flotante
        x = 1
    if x < -1:
        x = -1
    return (math.acos(x))

def calculate_angle_vectors(point_x, point_y, point_z) -> float:
    """
    Calculates angle between three waypoints
    in radians
    """
    # calculate A (X->Y) and B (Y->Z) vectors
    a_x = point_x.x - point_y.x
    a_y = point_x.y - point_y.y
    a_z = point_x.z - point_y.z

    b_x =  point_z.x - point_y.x
    b_y =  point_z.y - point_y.y
    b_z =  point_z.z - point_y.z

    # dot product
    dot_product = a_x * b_x + a_y * b_y + a_z * b_z
    print(f"dot product: {dot_product}")

    #magnitudes
    mag_a = math.sqrt(a_x**2 + a_y**2 + a_z**2)
    print(f"mag a: {mag_a}")
    mag_b = math.sqrt(b_x**2 + b_y**2 + b_z**2)
    print(f"mag b: {mag_b}")

    x = dot_product/(mag_a*mag_b)
    if x > 1: # evita errores de dominio por la coma flotante
        x = 1
    if x < -1:
        x = -1
    return (math.acos(x))

def calculate_direction(a: PoseStamped, b: PoseStamped) -> Vector3:
    """
    Calculates direction between 2 points
    represented by a unit 3d vector
    """
    v = Vector3()
    x = b.pose.position.x - a.pose.position.x
    y = b.pose.position.y - a.pose.position.y
    z = b.pose.position.z - a.pose.position.z
    magnitude = math.sqrt(x*x + y*y + z*z)
    v.x = x/magnitude
    v.y = y/magnitude
    v.z = z/magnitude

    return v

def slerp(a, b, t) -> Vector3:
    """
    Slerp function
    """
    origin = Vector3()
    origin.x = 0.0
    origin.y = 0.0
    origin.z = 0.0

    omega = calculate_angle_vectors(a, origin, b) # calculates angle between the two directions

    r1 = math.sin(((1-t)*omega))/math.sin(omega)
    r2 = math.sin(t/omega)/math.sin(omega)

    a_x_r = r1 * a.x
    a_y_r = r1 * a.y
    a_z_r = r1 * a.z

    b_x_r = r2 * b.x
    b_y_r = r2 * b.y
    b_z_r = r2 * b.z

    result = Vector3()
    result.x = a_x_r + b_x_r
    result.y = a_y_r + b_y_r
    result.z = a_z_r + b_z_r

    mag = math.sqrt(result.x**2 + result.y**2 + result.z**2)

    result.x = result.x/mag
    result.y = result.y/mag
    result.z = result.z/mag

    return result

def lerp(a: float, b: float, t: float) -> float:
    """
    Lerp function
    """
    return (1 - t) * a + t * b

def calculate_near_point(vf, vi) -> float:
    return abs(vf**2 - vi**2)/(2*(MAX_ACCELERATION*0.85))

def print_vec(v):
    print(f"[{v.x},{v.y},{v.z}]")

def print_point(a):
    print(f"({a.pose.position.x},{a.pose.position.y},{a.pose.position.z})")

def main():
    # global path_publisher

    rclpy.init()
    pose_subscriber = Subscriber()
    rclpy.spin(pose_subscriber)
    # rclpy.spin(path_publisher)
