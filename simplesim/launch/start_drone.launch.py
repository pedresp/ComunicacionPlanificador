import launch
from launch import LaunchContext, LaunchDescriptionEntity
from launch.actions import DeclareLaunchArgument, OpaqueFunction, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory

'''
Estas dos funciones son necesarias porque los Launch Configuration no se procesan hasta el runtime 
esto causa que no sea posible concatenar el valor string que tiene dentro con otro string,
pues se consideran clases distintas.
Dado que lo necesito para poder encontrar la ruta de los ficheros YAML necesito usar una 
OpaqueFunction y un context.perform_substitution() que permiten obtener el valor string
que el Launch Configuration tiene dentro.
'''

def get_configuration_with_context(context: LaunchContext, drone_id):
    drone_config_str = context.perform_substitution(LaunchConfiguration('drone_config'))
    
    config = os.path.join(
        get_package_share_directory('simplesim'),
        'config',
        drone_config_str
    )

    return [launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='simulator',
        name='simulator',
        parameters=[config]
    )]

def get_wps_with_context(context: LaunchContext, drone_id):
    drone_wps_str = context.perform_substitution(LaunchConfiguration('drone_wps'))

    wps = os.path.join(
        get_package_share_directory('simplesim'),
        'waypoints',
        drone_wps_str
    )

    return [launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='controller',
        name='controller',
        parameters=[wps]
    )]

def generate_launch_description():
    drone_id = LaunchConfiguration('drone_id', default='drone_x')

    drone_id_launch_arg = DeclareLaunchArgument(
        'drone_id',
        default_value='drone_x'
    )

    drone_config_launch_arg = DeclareLaunchArgument(
        'drone_config',
        default_value='drone_x.yaml'
    )

    drone_wps_launch_arg = DeclareLaunchArgument(
        'drone_wps',
        default_value='drone_x.yaml'
    )

    opaque_f_wps = OpaqueFunction(function=get_wps_with_context, args=[drone_id])

    opaque_f_config = OpaqueFunction(function=get_configuration_with_context, args=[drone_id])
    
    wps = launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='wp_vis',
        name='wps'
    )

    return launch.LaunchDescription([
        drone_id_launch_arg,
        drone_wps_launch_arg,
        drone_config_launch_arg,
        opaque_f_wps,
        # fp,
        opaque_f_config,
        wps,
        # ExecuteProcess(cmd=['echo', str(drone_wps_str) + str(entered) + ' + ' + str(drone_config_str) + str(entered2)],
                    #    output='screen'),
    ])