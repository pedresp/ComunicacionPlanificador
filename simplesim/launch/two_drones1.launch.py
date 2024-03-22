import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
#    for i in range(3):
    drone_name = 'drone_' + '1'
    fp = launch_ros.actions.Node(
        namespace=drone_name,
        package='simplesim',
        executable='fp',
        name='fp',
        parameters=['drone_id='+'1']
    )
    simulator = launch_ros.actions.Node(
        namespace=drone_name,
        package='simplesim',
        executable='simulator',
        name='simulator',
        parameters=['drone_id='+'1']
    )
    wps = launch_ros.actions.Node(
        namespace=drone_name,
        package='simplesim',
        executable='wp_vis',
        name='wps',
            parameters=['drone_id='+'1']
    )

    return launch.LaunchDescription([
        fp,
        simulator,
        wps
    ])