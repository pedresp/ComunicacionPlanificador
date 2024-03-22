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
    wp = launch_ros.actions.Node(
        namespace='drone_0',
        package='simplesim',
        executable='wp_vis',
        name='wp'
    )
    fp = launch_ros.actions.Node(
        namespace='drone_0',
        package='simplesim',
        executable='fp',
        name='fp'
    )

    return launch.LaunchDescription([
        rviz_node,
        wp,
        fp,
    ])