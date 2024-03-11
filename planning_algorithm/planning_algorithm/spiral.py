from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
from math import ceil, atan2, pi, floor, sqrt,atan,cos 
from matplotlib import path
from numpy import linalg as LA
from pyclothoids import Clothoid
from pyclothoids import SolveG2
from .graphical_info import *


def convex_hull_fun(polygon_sides):
    hull = ConvexHull(polygon_sides)
    return polygon_sides[hull.vertices,:]

def centroid(vertexes):
    x_list = [vertex [0] for vertex in vertexes]
    y_list = [vertex [1] for vertex in vertexes]
    lenv = len(vertexes)
    x = sum(x_list) / lenv
    y = sum(y_list) / lenv
    centroid=np.array([x,y])
    return centroid

def get_dcp(points,centroid): #hallar la minima distancia de un lado al centroide
    #d = norm(np.cross(p2-p1, p1-p3))/norm(p2-p1) ....p3 es el centroide y p1 y p2 los puntos de la recta
    number_of_sides=len(points)
    distance_matrix=np.zeros((number_of_sides))
    limit_points=np.array(points)
    for i in range(0,number_of_sides):
        if (i+1)<number_of_sides:
            distance_matrix[i]=LA.norm(np.cross(limit_points[i+1,:]-limit_points[i,:],limit_points[i,:]-centroid))/LA.norm(limit_points[i+1,:]-limit_points[i,:])
        else:
            distance_matrix[i]=LA.norm(np.cross(limit_points[0,:]-limit_points[i,:],limit_points[i,:]-centroid))/LA.norm(limit_points[0,:]-limit_points[i,:])

    dcp=np.amin(distance_matrix)
    return dcp




def get_first_point(po,pf,street_spacing):
    segments=(LA.norm(pf-po)/street_spacing)
    x_delta=(pf[0]-po[0])/ segments
    y_delta=(pf[1]-po[1])/ segments
    
    
    point=np.array([po[0] + x_delta, po[1] + y_delta,1])
    
    return point


def GetAngleOfLineBetweenTwoPoints(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    return atan2(yDiff, xDiff)


def get_internal_first_polygon(limit_points,spacing):

    cp=centroid(limit_points)
    distance=LA.norm(cp-limit_points[1])


    limit_points_list=[]

    nr=round(float(distance)/float(0.5*spacing))

    scale=0.9#(nr-1)/nr 
    new_polygon=scale_polygon(limit_points,scale)

    return new_polygon





def order_points(UAV,polygon_points):
    distance_list=[]
    final_polygon_points=[]
    ini_point=centroid(UAV)
    for point in polygon_points:
        dist=LA.norm(ini_point-point)
        distance_list.append(dist)

    #get the minimum distance in the list
    min_dist = min(distance_list)

    #return the index of minimum value 
    min_index=distance_list.index(min_dist)

    polygon_size=len(polygon_points)

    #calculate the angle between centroid and the min point
    line_angle=GetAngleOfLineBetweenTwoPoints(ini_point,polygon_points[min_index])

    #Choose CW or CCW direction of spiral
    if min_index==(polygon_size-1):
        ccw_angle=GetAngleOfLineBetweenTwoPoints(polygon_points[min_index],polygon_points[0])
        cw_angle=GetAngleOfLineBetweenTwoPoints(polygon_points[min_index],polygon_points[min_index-1])
        
    else:
        ccw_angle=GetAngleOfLineBetweenTwoPoints(polygon_points[min_index],polygon_points[min_index+1])
        cw_angle=GetAngleOfLineBetweenTwoPoints(polygon_points[min_index],polygon_points[min_index-1])
    #second_angle1=GetAngleOfLineBetweenTwoPoints(ini_point,polygon_points[min_index])
    diff1=abs(line_angle-cw_angle)
    diif2=abs(line_angle-ccw_angle)

    if diff1<diif2:
        CW=True
    else:
        CW=False
    
    if CW:
        """
        if min_index==0: #Evita error en la función range !=0
            final_polygon_points.append(polygon_points[0])
            for k in range(polygon_size-1,-1,0):
                final_polygon_points.append(polygon_points[0])
        """

        #else:
        for i in range(min_index, -1, -1) :
            final_polygon_points.append(polygon_points[i])
   
        for j in reversed(range (min_index+1,polygon_size)):
            final_polygon_points.append(polygon_points[j])
         


    else:
        for i in range(min_index, polygon_size) :
            final_polygon_points.append(polygon_points[i])
        for j in range (0,min_index):
            final_polygon_points.append(polygon_points[j])


    return final_polygon_points



def spiral_affine(limit_points,street_spacing):


    cp=centroid(limit_points)
    dcp=get_dcp(limit_points,cp)

    #generamos mas lineas paralelas de las necesarias para la prueba
    nr=ceil(float(dcp)/float(street_spacing))
    
    #se debe agregar un punto con el valor de 1 a cada coordenada 
    # para que la matriz quede del mismo tamaño  
    limit_points=np.c_[ limit_points, np.ones(len(limit_points))] 
    
    #desplazar primero la espiral al centro 
    xc=cp[0]
    yc=cp[1]
    T_s0 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])

    center_polygon=[]

    for row in limit_points:
        output_row = T_s0 @ row
        x_s, y_s, i_s = output_row
        center_polygon.append(np.array([x_s,y_s,1]))


    center_spiral=[]

    #escalar en iteraciones
    
    for i in range (0,(nr)):
        scale=(nr-i)/nr
        if scale>0:
            T_s = np.array([[scale, 0, 0], [0, scale, 0], [0, 0, 1]]) #Escalar en cada iteracion
            scale_polygon=[]
        
            for row in center_polygon:
                output_row = T_s @ row
                x_s, y_s, i_s = output_row
                scale_polygon.append(np.array([x_s,y_s,1]))
            
        
            first_point=get_first_point(scale_polygon[0],scale_polygon[-1],street_spacing)
            #eliminar el punto
            #scale_polygon.pop(0) #no lo eliminamos
            center_spiral=center_spiral+scale_polygon
        

            #center_spiral.append(first_point)
  
    
    #volver a desplazar los puntos a su sitio
    T_sf = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])

    final_spiral=[]

    for row in center_spiral:
        output_row = T_sf @ row
        x_s, y_s, i_s = output_row
        final_spiral.append(np.array([x_s,y_s]))
        
    #final_spiral.insert(0,np.array([limit_points[0,0],limit_points[0,1]]))
    #final_spiral.append(np.array([xc,yc])) Centroide
    
        
    sampled=np.array(final_spiral) 
        
        
    return sampled



def split(start, end, spacing):

    dist=LA.norm(start-end)
    segments=ceil(dist/spacing)
  
    if (segments<=1):
        segments=2


    x_delta = (end[0] - start[0]) / (segments)
    y_delta = (end[1] - start[1]) / (segments)
    points=np.zeros((2 ,2))
    ini=np.zeros((1,2))
    ini[0,:]=[start[0], start[1]]
    fin=np.zeros((1,2))
    fin[0,:]=[end[0], end[1]]
    #points = []
    
    
    points[0,:]=[start[0] + 1 * x_delta, start[1] + 1 * y_delta]
    points[1,:]=[start[0] + (segments-1) * x_delta, start[1] + (segments-1) * y_delta]
    
    #for i in range(1, segments):
    #    points[i-1,:]=[start[0] + i * x_delta, start[1] + i * y_delta]

    #points_final=np.concatenate((ini,points,fin),axis=0)
    
    
    #La mejor idea es devolver unicamente el primer y el ultimo punto 
    
    return points


def split_waypoints(start, end, segments):

    if segments==0:
        ini=np.zeros((1,2))
        ini[0,:]=[start[0], start[1]]
        fin=np.zeros((1,2))
        fin[0,:]=[end[0], end[1]]
        points=np.concatenate((ini,fin),axis=0)
        return points
    
    else:

        x_delta = (end[0] - start[0]) / float(segments)
        y_delta = (end[1] - start[1]) / float(segments)
        ini=np.zeros((1,2))
        ini[0,:]=[start[0], start[1]]
        fin=np.zeros((1,2))
        fin[0,:]=[end[0], end[1]]
        points=np.zeros((segments ,2))
        #points = []
        
        for i in range(0, segments):
            points[i,:]=[start[0] + i * x_delta, start[1] + i * y_delta]

        points=np.delete(points,0,axis=0)
        
        #print(start)
        points_b=np.concatenate((ini, points),axis=0)
        points_c=np.concatenate((points_b,fin),axis=0)
        return points_c



def sampled_spiral(spiral_wpts, spacing):

    dist=LA.norm(spiral_wpts[0,:]-spiral_wpts[1,:])
    split_val=ceil(dist/spacing)
  
    if (split_val<=0):
        split_val=1
    
    

    prev_array=split(spiral_wpts[0,:],spiral_wpts[1,:], split_val)



    for i in range (1,int(len(spiral_wpts)-1)):
        dist=LA.norm(spiral_wpts[i,:]-spiral_wpts[i+1,:])
        split_val=floor(dist/spacing)
        if (split_val<=0):
            split_val=1

        current_array=split(spiral_wpts[i,:],spiral_wpts[i+1,:], split_val)
        current_array=current_array[1:]
        #print(current_array)
        final=np.concatenate((prev_array,current_array),axis=0)
        prev_array=final
    
    return final


def get_angle_list(points):
    angle_list=[]
    for i in range(0,len(points)-1):
        angle=GetAngleOfLineBetweenTwoPoints(points[i,:],points[i+1,:])
        angle_list.append(angle)
    
    angle=GetAngleOfLineBetweenTwoPoints(points[len(points)-1,:],points[0,:])
    angle_list.append(angle)
    
    return angle_list




def clothoid_waypoints(wpts,spacing,samples):

    merged_points=[]

    merged_points.append(wpts[0,:])


    point_array=split(wpts[0,:],wpts[1,:],spacing)

    for i in range (1,(len(wpts)-1)):
        points=split(wpts[i,:],wpts[i+1,:],spacing)
        point_array=np.concatenate((point_array,points),axis=0)
        
    #print(point_array)


    for i in range (0,len(wpts)-2):
        angle_o=GetAngleOfLineBetweenTwoPoints(wpts[i,:],wpts[i+1,:])
        angle_f=GetAngleOfLineBetweenTwoPoints(wpts[i+1,:],wpts[i+2,:])


        clothoid1 = Clothoid.G1Hermite(point_array[(2*i)+1,0], point_array[(2*i)+1,1], angle_o, point_array[(2*i)+2,0], point_array[(2*i)+2,1],angle_f)
        x,y=clothoid1.SampleXY(samples)

        points=list(zip(x, y))        

        merged_points.extend(points)
    
    merged_points.append(wpts[-1,:])

    return merged_points



def scale_polygon(limit_points, scale):

    cp=centroid(limit_points)
    #se debe agregar un punto con el valor de 1 a cada coordenada 
    # para que la matriz quede del mismo tamaño  
    limit_points=np.c_[ limit_points, np.ones(len(limit_points))] 
    
    #desplazar primero la espiral al centro 
    xc=cp[0]
    yc=cp[1]
    T_s0 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])

    center_polygon=[]

    for row in limit_points:
        output_row = T_s0 @ row
        x_s, y_s, i_s = output_row
        center_polygon.append(np.array([x_s,y_s,1]))
    

    T_s = np.array([[scale, 0, 0], [0, scale, 0], [0, 0, 1]]) #Escalar en cada iteracion
    
    scale_polygon=[]
        
    for row in center_polygon:
        output_row = T_s @ row
        x_s, y_s, i_s = output_row
        scale_polygon.append(np.array([x_s,y_s,1]))
            
  
    
    #volver a desplazar los puntos a su sitio
    T_sf = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])

    final_polygon=[]

    for row in scale_polygon:
        output_row = T_sf @ row
        x_s, y_s, i_s = output_row
        final_polygon.append(np.array([x_s,y_s]))
   

    return final_polygon




def get_internal_limits(numberofUAVS,limit_points,str_space):

    cp=centroid(limit_points)
    dcp=get_dcp(limit_points,cp)

    limit_points_list=[]

    nr=ceil(float(dcp)/float(str_space))+1
    print(nr)
    

    for i in range (0,numberofUAVS):
        scale=(nr-i)/nr 
        current_limits=scale_polygon(limit_points,scale)
        limit_points_list.append(current_limits)
    
    return limit_points_list




def get_scales(numberofUAV, limit_points,str_space):
    
    scales = [[] for _ in range(numberofUAV)]

    cp=centroid(limit_points)
    dcp=get_dcp(limit_points,cp)
    nr=ceil(float(dcp)/float(str_space))+1

    scale_list=[]

    for i in range(0,nr):
        current_scale=(nr-i)/nr
        scale_list.append(current_scale)
    
    for i, element in enumerate(scale_list):
        set_index = i % numberofUAV
        scales[set_index].append(element)
    
    return scales




def multiple_spiral_affine(limit_points,scale_list,str_spacing):

    cp=centroid(limit_points)
    
    #se debe agregar un punto con el valor de 1 a cada coordenada 
    # para que la matriz quede del mismo tamaño  
    limit_points=np.c_[ limit_points, np.ones(len(limit_points))] 
    
    #desplazar primero la espiral al centro 
    xc=cp[0]
    yc=cp[1]
    T_s0 = np.array([[1, 0, -xc], [0, 1, -yc], [0, 0, 1]])

    center_polygon=[]

    for row in limit_points:
        output_row = T_s0 @ row
        x_s, y_s, i_s = output_row
        center_polygon.append(np.array([x_s,y_s,1]))


    center_spiral=[]

    #escalar en iteraciones
    for i in range (0,len(scale_list)):
        T_s = np.array([[scale_list[i], 0, 0], [0, scale_list[i], 0], [0, 0, 1]]) #Escalar en cada iteracion
        scale_polygon=[]
        
        for row in center_polygon:
            output_row = T_s @ row
            x_s, y_s, i_s = output_row
            scale_polygon.append(np.array([x_s,y_s,1]))
            
        
        first_point=get_first_point(scale_polygon[0],scale_polygon[-1],str_spacing)
        #eliminar el punto
        if i!=0:
            scale_polygon.pop(0) 
        center_spiral=center_spiral+scale_polygon
        
        

        center_spiral.append(first_point)
    
    #volver a desplazar los puntos a su sitio
    T_sf = np.array([[1, 0, xc], [0, 1, yc], [0, 0, 1]])

    final_spiral=[]

    for row in center_spiral:
        output_row = T_sf @ row
        x_s, y_s, i_s = output_row
        final_spiral.append(np.array([x_s,y_s]))
        
    #final_spiral.insert(0,np.array([limit_points[0,0],limit_points[0,1]]))
    #final_spiral.append(np.array([xc,yc])) Centroide
    
        
    sampled=np.array(final_spiral) 
        
        
    return sampled
                


def initial_points(first_point, final_point, distance, n):
    # Calcula la ecuación de la recta que pasa por los dos puntos
    slope = (final_point[1] - first_point[1]) / (final_point[0] - first_point[0])
    ordenada_origen = first_point[1] - slope * first_point[0]
    angle=atan(slope)

    # Calcula los puntos que están a la distancia definida desde el punto de referencia
    delta_x =  distance* cos(angle)
    points = []


    for i in range(n):
        x = first_point[0] + delta_x * i
        y = slope * x + ordenada_origen
        points.append((x, y))

    return points

    
    
"""
def get_multiple_spirals(UAV,limit_points,street_spacing,waypoint_distance):
    UAVnumber=len(UAV)
    cp=centroid(limit_points)

    scale_list=get_scales(UAVnumber,limit_points,street_spacing)
    
    spiral_list=[]

    for scales in scale_list:
        current_spiral_wpts=multiple_spiral_affine(limit_points,scales,street_spacing)
        clothoid_spiral=clothoid_waypoints(current_spiral_wpts,waypoint_distance,30)
        
        spiral_list.append(clothoid_spiral)
    
   
    points=initial_points(limit_points[0],cp,street_spacing,UAVnumber-1)
    
    print(points)




    return spiral_list

"""


    

def get_spirals(polygon_list, spacing_list, wpt_separation, UAV_list):

    UAV_coords=[]



    for UAV in UAV_list:
        coords=[UAV[0], UAV[1]]
        UAV_coords.append(np.array(coords))
    
    


    spiral_list=[]
    i=0

    for polygon in polygon_list:
        limit_points=order_points(UAV_coords,polygon)
        internal_limits=get_internal_first_polygon(limit_points,spacing_list[i])
        samples=20
        spiral_wpts= spiral_affine(internal_limits,spacing_list[i])
        clothoid_wpts=np.array(clothoid_waypoints(spiral_wpts,wpt_separation,samples))
        spiral_list.append(clothoid_wpts)
        i+=1

    return spiral_list
