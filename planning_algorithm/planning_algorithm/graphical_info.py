import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.spatial import ConvexHull

import scipy
import numpy as np

#Axis to get the graphical info
xmin=-200
xmax=200
ymin=-200
ymax=200


def convex_hull_fun(polygon_sides):
    hull = ConvexHull(polygon_sides)
    return polygon_sides[hull.vertices,:]

def get_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0  # No es un polígono válido

    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2.0
    return area


def get_polygon(number_of_sides):
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid(True)
    limit_points=np.array(plt.ginput(number_of_sides))
    x=limit_points[:,0]
    y=limit_points[:,1]
    return limit_points,x,y

def get_polygon2(points_collection):
    limit_points=np.empty((0,2))
    for point in points_collection:
        limit_points=np.append(limit_points, [[point['x'], point['y']]], axis=0)
    x=limit_points[:,0]
    y=limit_points[:,1]
    return limit_points,x,y

def draw_polygons(polygon_list):

    for polygon in polygon_list:

        polygon_array=np.array(polygon)
        xP=polygon_array[:,0]
        xP1=np.append(xP,xP[0])
        yP=polygon_array[:,1]
        yP1=np.append(yP,yP[0])
        plt.plot(xP1,yP1)

    """
    for polygon in polygon_list:
        polygon_array=np.array(polygon)
        xP=polygon_array[:,0]
        yP=polygon_array[:,1]


        plt.plot(xP,yP)
    """

    plt.draw()
    plt.show()


def draw_multi_plans(polygon, spiral_wpts):

    polygon_array=np.array(polygon)
    xP=polygon_array[:,0]
    xP1=np.append(xP,xP[0])
    yP=polygon_array[:,1]
    yP1=np.append(yP,yP[0])
    plt.plot(xP1,yP1)
    """
    for polygon in polygon_list:

        polygon_array=np.array(polygon)
        xP=polygon_array[:,0]
        xP1=np.append(xP,xP[0])
        yP=polygon_array[:,1]
        yP1=np.append(yP,yP[0])
        plt.plot(xP1,yP1)
    """

    for spiral in spiral_wpts:
        spiral=np.array(spiral)
        xC=spiral[:,0]
        yC=spiral[:,1]
        plt.plot(xC,yC)

    """
    for polygon in polygon_list:
        polygon_array=np.array(polygon)
        xP=polygon_array[:,0]
        yP=polygon_array[:,1]


        plt.plot(xP,yP)
    """

    plt.draw()
    plt.show()


def get_sim_uavs(number_of_uavs):
    plt.axis([xmin, xmax, ymin, ymax])
    uavs=np.array(plt.ginput(number_of_uavs))
    return uavs

def draw_all(UAV,limit_points,spiral_wpts,clothoid_wpts):
    
    xP=limit_points[:,0]
    np.append(xP,xP[0])
    yP=limit_points[:,1]
    np.append(yP,yP[0])
    plt.scatter(xP,yP)

    xU=UAV[:,0]
    yU=UAV[:,1]
    plt.scatter(xU,yU)

    #xS=spiral_wpts[:,0]
    #yS=spiral_wpts[:,1]
    #plt.plot(xS,yS)

    xC=clothoid_wpts[:,0]
    yC=clothoid_wpts[:,1]
    plt.plot(xC,yC)


    plt.draw()
    plt.show()


def draw_multi(UAV,limit_points,spiral_wpts):
    limit_points=np.array(limit_points)
    xP=limit_points[:,0]
    np.append(xP,xP[0])
    yP=limit_points[:,1]
    np.append(yP,yP[0])
    plt.plot(xP,yP)

    xU=UAV[:,0]
    yU=UAV[:,1]
    plt.scatter(xU,yU)

    #xS=spiral_wpts[:,0]
    #yS=spiral_wpts[:,1]
    #plt.plot(xS,yS)
    for spiral in spiral_wpts:
        spiral=np.array(spiral)
        xC=spiral[:,0]
        yC=spiral[:,1]
        plt.plot(xC,yC)


    plt.draw()
    plt.show()


def draw_final_plans(coords,limit_points,waypoint_list):
    polygon_array=np.array(limit_points)
    xP=polygon_array[:,0]
    xP1=np.append(xP,xP[0])
    yP=polygon_array[:,1]
    yP1=np.append(yP,yP[0])
    
    """
    for coord in coords:
        xU=np.array(coord)[:,0]
        yU=np.array(coord)[:,1]
        plt.scatter(xU,yU)
    """
    
    k=0
    num=0
    leg=[]
    fig, ax = plt.subplots()    

    for waypoints in waypoint_list:

        
        waypoint_matrix=np.array(waypoints)
        UAV=np.array(coords[k])
        
        
        final_waypoint_matrix=np.ones((len(waypoint_matrix),len(waypoint_matrix[0])+2,2))*float("NaN")
        for i in range(0,len(UAV)):                 #add first waypoint
            
            final_waypoint_matrix[i,0,:]=UAV[i,:]

        for i in range(0,len(UAV)):    #add next and last waypoint
            for j in range (0, len(waypoint_matrix[0])):
                if not np.isnan(waypoint_matrix[i, j, 1]):
                    final_waypoint_matrix[i,j+1,:]=waypoint_matrix[i,j,:]
                    final_waypoint_matrix[i,j+2,:]=UAV[i,:]
                    
        
        for i in range(0,len(UAV)):
            label_uav="UAV "+str(num)
            ax.plot(final_waypoint_matrix[i,:,0],final_waypoint_matrix[i,:,1],label=label_uav)
            num=num+1
            ax.axis('equal')
            leg = ax.legend(loc="lower left")
             
        k=k+1

    ax.plot(xP1,yP1,'--k',)
    plt.draw()
    plt.grid()
    plt.title("UAV Trajectories")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
