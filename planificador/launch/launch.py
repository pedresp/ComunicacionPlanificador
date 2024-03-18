from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='planificador',
            executable='client',
            name='drone_0',
            parameters=[
                {'drone_id': 'drone_0'},
                {'speed': 20.0},
                {'tof': 52.2},
                {'ancho_de_barrido': 33.0},
                {'coordx': -200.0},
                {'coordy': 0.0}
            ]
        ),
        
        Node(
            package='planificador',
            executable='client',
            name='drone_1',
            parameters=[
                {'drone_id': 'drone_1'},
                {'speed': 20.0},
                {'tof': 52.2},
                {'ancho_de_barrido': 33.0},
                {'coordx': -200.0},
                {'coordy': 0.0}
            ]
        ),

        Node(
            package='planificador',
            executable='client',
            name='drone_2',
            parameters=[
                {'drone_id': 'drone_2'},
                {'speed': 20.0},
                {'tof': 52.2},
                {'ancho_de_barrido': 13.0},
                {'coordx': -200.0},
                {'coordy': 0.0}
            ]
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