import os
import launch_ros
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_file = 'mult_config.rviz'
    config = os.path.join(
        get_package_share_directory('simplesim'),
        'rviz',
        config_file
    )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d' + config]
    )

    drone_0 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_0',
            'drone_config':'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )
    
    drone_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_1',
            'drone_config':'drone_1.yaml'
        }.items()
    )

    drone_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_2'
        }.items()
    )

    return LaunchDescription([
            rviz_node,
            drone_0,
            # drone_1,
            # drone_2
        ])