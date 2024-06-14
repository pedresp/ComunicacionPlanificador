import os
import launch_ros
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_file = 'rosviz-conf.rviz'
    config = os.path.join(
        get_package_share_directory('scenariovis'),
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

    area = launch_ros.actions.Node(
        package="scenariovis",
        executable="areavis",
        name="areavis"
    ) 

    visman = launch_ros.actions.Node(
        package='scenariovis',
        executable='visman',
        name='visman'
    )
    
    return LaunchDescription([
            rviz_node,
            area,
            visman
        ])