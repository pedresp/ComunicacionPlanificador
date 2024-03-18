###############################################
# Multiple Heterogeneous UAV CPP              #
# Author: Marco Luna                          #
###############################################
#Se debe ejecutar con python3
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import time
#import csv

#Math
import numpy as np


#Own libraries
from .graphical_info import *
from .polygon_division import *
from .heterogeneous_calculation import *
from .spiral import *

from .back_and_forth import *

from .readcsv import readUAV
import yaml
import rospkg
import os

# opening the 'csv' file for testing

#with open('UAV.csv', newline = '') as file:
   
#    reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC,
#                        delimiter = ',')
     
    # storing all the rows in an output list
#    UAVs = []
#    for row in reader:
#        UAVs.append(row[:])
def verdugo(drones, path_to_area_coord: str):
    #UAVs = readUAV()
    UAVs = drones

    #Initial parameters
    # changed and commented loc to allow points selection from a yaml file
    perimeter = {}
    with open(path_to_area_coord, 'r') as file:
        perimeter = yaml.safe_load(file)
    #polygon_sides=6
    wpt_separation=10
    print("el perimetro es:", perimeter)
    print('Select the points for this area:')
    #limits,x,y=get_polygon(polygon_sides)
    limits,x,y=get_polygon2(perimeter['areas'][0]['area']['coords'])

    convex_limits=convex_hull_fun(limits)

    start=time.time()
    total_area=get_polygon_area(convex_limits)

    scores=get_UAV_score_list(UAVs, total_area)

    #UAV score dictionary
    scan_dict=classify_by_scan(UAVs, scores)

    print (scan_dict)
    #print (w_class)


    weights_vector=get_area_weights(scan_dict)
    weights=(np.array(weights_vector))[:,1]
    spacings=(np.array(weights_vector))[:,0]

    #generate subareas
    polygons= get_pode_parts(convex_limits,weights)


    #spirals=get_spirals(polygons, spacings, wpt_separation, UAVs)
    bf_list=multibf(polygons,spacings,wpt_separation,UAVs)



    weight_list, coords_list=get_weight_and_coord_list(UAVs,scan_dict)

    #waypoint_list, cost_list= final_assingment(weight_list,coords_list,spirals)
    waypoint_list, cost_list= final_assingment(weight_list,coords_list,bf_list)

    end=time.time()
    print("waypoint list:", waypoint_list)

    print("weight list:", scores)
    print("Cost list:", cost_list)



    draw_polygons(polygons)


    #draw_multi_plans(convex_limits,spirals)
    draw_multi_plans(convex_limits,bf_list)



    draw_final_plans(coords_list,convex_limits,waypoint_list)
    print("Elapsed time:",(end-start))

    return waypoint_list


if __name__ == '__main__':
    UAVs = [[-200.0, 0.0, 20.0, 30.0, 48.0], [-200.0, 0.0, 10.0, 40.0, 41.0], [-200.0, 0.0, 15.0, 20.0, 81.0], [-200.0, 0.0, 5.0, 10.0, 56.0]]
    #verdugo(UAVs)