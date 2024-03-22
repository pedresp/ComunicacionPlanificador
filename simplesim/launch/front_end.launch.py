import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_file = 'config.rviz'
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
    fp = launch_ros.actions.Node(
        package='simplesim',
        executable='fp',
        name='fp'
    )
    simulator = launch_ros.actions.Node(
        package='simplesim',
        executable='simulator',
        name='simulator'
    )
    wps = launch_ros.actions.Node(
        package='simplesim',
        executable='wp_vis',
        name='wps'
    )

    return launch.LaunchDescription([
        rviz_node,
        fp,
        simulator,
        wps
    ])