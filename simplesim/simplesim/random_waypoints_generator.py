from geometry_msgs.msg import PoseStamped
import random

def generate_random_waypoints(distance_between, number):
    initPos = PoseStamped()

    initPos.pose.position.x = 0.0
    initPos.pose.position.y = 0.0
    initPos.pose.position.z = 0.0
    
    wps = [initPos]
    for i in range(1,number):
        newPos = PoseStamped()
        
        x = wps[-1].pose.position.x + distance_between * (random_pos_neg())
        y = wps[-1].pose.position.y + distance_between * (random_pos_neg())
        z = wps[-1].pose.position.z + distance_between * (random_pos_neg())

        newPos.pose.position.x = x
        newPos.pose.position.y = y
        newPos.pose.position.z = z

        wps.append(newPos)

    return wps

def random_pos_neg():
    return 1 if random.random() < 0.5 else -1