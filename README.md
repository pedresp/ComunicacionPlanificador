## ComunicacionPlanificador

Este repositorio contiene el código del TFG desarrollado en el grupo de 
investigación CVAR. 

Incluye un entorno de pruebas para algoritmos de planificación
automática orientados a sistemas robóticos aéreos y una herramienta para la 
visualización de estas trayectorias. Para obtener más información se recomienda leer
la memoria asociada con este proyecto.

## Cómo usar

Para hacer uso del entorno es recomendable usar la herramienta 
[DSUT](https://github.com/pedresp/DSUT).

En primer lugar se debe crear un workspace ROS2 e importar el repositorio:

```bash
mkdir -p ~/ros_tfg/src
cd ~/ros_tfg/src

git clone https://github.com/pedresp/ComunicacionPlanificador.git

cd ..
rosdep install -i --from-path src --rosdistro humble -y
```

Posteriormente se debe ejecutar y generar la configuración deseada tal y cómo se 
indica en su repositorio. 

Una vez se ha generado los archivos de configuración, para ejecutar el entorno de 
pruebas se deben ejecutar los siguientes mandatos:
```bash
cd ~/ros_tfg
colcon build
. install/setup.bash
ros2 launch simplesim my_launcher_drones.launch.py
```

Cuando todos los drones hayan vuelto a su punto de despegue, se debe parar la
ejecución del programa pulsando Ctrl + C en la terminal.

Para visualizar las trayectorias de la simulación, almacenadas en el directorio ```~/sim_stats/```, se debe ejecutar el visualizador de trayectorias, ScVis:

```bash
cd ~/ros_tfg
ros2 launch scenariovis python.launch.py 
```

### Menciones

Los paquetes ```simplesim``` y ```sim_msgs``` pertenecen al repositorio 
[multiple_drones_sim](https://github.com/anastmur/multiple_drones_sim). El paquete
incluye el algoritmo de planificación CoP-BINPAT desarrollado por Marco A. Luna 
explicado en el artículo "Técnicas de planificación de rutas de cobertura de área y
gestión dinámica de misiones para sistemas multi-UAV"(próxima presentación).