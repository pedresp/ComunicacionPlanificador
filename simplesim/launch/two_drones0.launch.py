import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
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
#    for i in range(3):
    drone_name = 'drone_' + '0'
    fp = launch_ros.actions.Node(
        namespace=drone_name,
        package='simplesim',
        executable='fp',
        name='fp',
        parameters=['drone_id='+'0']
    )
    simulator = launch_ros.actions.Node(
        namespace=drone_name,
        package='simplesim',
        executable='simulator',
        name='simulator',
        parameters=['drone_id='+'0']
    )
    wps = launch_ros.actions.Node(
        namespace=drone_name,
        package='simplesim',
        executable='wp_vis',
        name='wps',
            parameters=['drone_id='+'0']
    )

    return launch.LaunchDescription([
        rviz_node,
        fp,
        simulator,
        wps
    ])