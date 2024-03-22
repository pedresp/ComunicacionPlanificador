from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_file = 'mult_config.rviz'
    config = os.path.join(
        get_package_share_directory('simplesim'),
        'rviz',
        config_file
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d' + config]
    )
    return LaunchDescription([
        rviz_node,
        Node(
            namespace='drone_0',
            package='simplesim',
            executable='controller',
            name='controller',
            parameters=[{'drone_id': 'drone_0'}]
        ),
        Node(
            namespace='drone_0',
            package='simplesim',
            executable='wp_vis',
            name='wps'
        ),
        Node(
            namespace='drone_0',
            package='simplesim',
            executable='simulator',
            name='simulator',
            parameters=[{'speed': 20.0}]
        ),
        Node(
            namespace='drone_1',
            package='simplesim',
            executable='controller',
            name='controller',
             parameters=[{'drone_id': 'drone_1'}]
        ),
        Node(
            namespace='drone_1',
            package='simplesim',
            executable='wp_vis',
            name='wps'
        ),
        Node(
            namespace='drone_1',
            package='simplesim',
            executable='simulator',
            name='simulator',
            parameters=[{'speed': 20.0}]
        ),
        Node(
            namespace='drone_2',
            package='simplesim',
            executable='controller',
            name='controller',
             parameters=[{'drone_id': 'drone_2'}]
        ),
        Node(
            namespace='drone_2',
            package='simplesim',
            executable='wp_vis',
            name='wps'
        ),
        Node(
            namespace='drone_2',
            package='simplesim',
            executable='simulator',
            name='simulator',
            parameters=[{'speed': 20.0}]
        ),
        Node(
          package='planificador',
          executable='server',
          name='server1',
          parameters=[
              {'drones_quantity': 3.0},
              {'flight_height': 8.0}
          ]  
        )
        
    ])