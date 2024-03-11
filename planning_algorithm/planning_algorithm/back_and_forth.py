import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from py2d.Math import Polygon, Vector


import numpy as np
import math
from matplotlib import path
from numpy import linalg as LA


def draw_waypoints (waypoint_matrix):
    
    #plot_map()
    plt.scatter(waypoint_matrix[:,0],waypoint_matrix[:,1])
 

    plt.draw()
    plt.show()




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




def get_internal_first_polygon(limits):

    limit_points=np.array(limits)
    cp=centroid(limit_points)


    #nr=round(float(distance)/float(0.5*spacing))

    scale=0.98#(nr-1)/nr 
    new_polygon=scale_polygon(limit_points,scale)

    return new_polygon

    
def centroid(vertexes):
    x_list = [vertex [0] for vertex in vertexes]
    y_list = [vertex [1] for vertex in vertexes]
    lenv = len(vertexes)
    x = sum(x_list) / lenv
    y = sum(y_list) / lenv
    centroid=np.array([x,y])
    return centroid




def split(start, end, segments):
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


def back_and_forth(point_list,spacing, separation, UAV):

    points=np.array(point_list)
    #Track generation
    x=points[:,0]
    y=points[:,1]

    areaWidth = max(x)-min(x)
    thetamin = 0


    #Get optimal direction
    for i in range(1, 360):
        theta=i*2*math.pi/360
        R=np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
        aux=R.dot(np.transpose(points))
        if (max(aux[0,:])-min(aux[0,:])) < areaWidth:
            areaWidth = max(aux[0,:])-min(aux[0,:])
            thetamin = theta

    R=np.array([[math.cos(thetamin), -math.sin(thetamin)], [math.sin(thetamin), math.cos(thetamin)]])
    aux=R.dot(np.transpose(points))
    x = np.transpose(aux[0,:])
    y = np.transpose(aux[1,:])

    areaWidth = max(x)-min(x)
    areaLength = max(y)-min(y)
    numberOfLanes = math.ceil(areaWidth/spacing)

    laneDist = areaWidth/(int(numberOfLanes))
    lanemin=np.zeros((int(numberOfLanes), 2))
    lanemax=np.zeros((int(numberOfLanes), 2))

    poly_points=np.zeros((x.size, 2))

    for i, val in enumerate(x):
        poly_points[i]=(x[i],y[i])

    p = path.Path(poly_points)


    for i in range(1, int(numberOfLanes+1)):
        xi=min(x)+laneDist*i-laneDist/2
        delta =0.1
        k = 0
        miny = min(y) + k*delta
        while not(p.contains_points([(xi, miny)])):
            miny=min(y)+k*delta
            k=k+1


        k=0
        maxy = max(y) - k*delta
        while not(p.contains_points([(xi, maxy)])):
            maxy=max(y)-k*delta
            k=k+1

        lanemin[i-1] = (xi,miny)
        lanemax[i-1] = (xi,maxy)

    lmin = np.transpose(np.transpose(R).dot(np.transpose(lanemin)))
    lmax = np.transpose(np.transpose(R).dot(np.transpose(lanemax)))


    V=np.zeros((int(numberOfLanes*2),2))
    for i in range(0, int(numberOfLanes*2)):

        if(i%2)==0:
            V[i,:]=lmax[int(i/2),:]
        else:
            V[i,:]=lmin[int((i-1)/2),:]

    #Intermediate waypoints

    prev_array=np.array(UAV)
    #first--decide the best initial point to generate tracks based on less V[0,:] or V[1,:] distance
    ini_mat=np.zeros((2,len(prev_array)))
    for i in range (0,len(prev_array)):
        ini_mat[0,i]=LA.norm(V[0,:]-prev_array[i,:])
        ini_mat[1,i]=LA.norm(V[1,:]-prev_array[i,:])
    

    result_min = np.where(ini_mat == np.amin(ini_mat)) #find the minimum distance
    prev_res=result_min[0][0]
    dist=LA.norm(V[0,:]-V[1,:]) #first track distance
    split_val=int(dist/separation)
    if split_val<1:
        split_val=1
    if(prev_res==0): #if minimum distance is for V0 start from V0
        prev_array=array=split(V[0,:], V[1,:], split_val)
    else:
        prev_array=array=split(V[1,:], V[0,:], split_val) 
    #plt.scatter(V[:,0],V[:,1])

    for i in range (1,int(len(V)/2)):
        dist=LA.norm(V[(2*i),:]-V[(2*i)+1,:])
        split_val=int(dist/separation)
        if split_val<1:
           split_val=1 #al menos dos waypoints en una calle
        if (prev_res==0):
            current_array=split(V[(2*i)+1,:], V[(2*i),:], split_val)# now change
            prev_res=1
        else:
            current_array=split(V[(2*i),:], V[(2*i)+1,:], split_val)
            prev_res=0
        final=np.concatenate((prev_array,current_array),axis=0)
        prev_array=final

   

    return final.tolist()



def multibf(polygon_list,spacing_list, separation, UAV_list):
    UAV_coords=[]



    for UAV in UAV_list:
        coords=[UAV[0], UAV[1]]
        UAV_coords.append(np.array(coords))
    
    


    bf_list=[]
    i=0

    for polygon in polygon_list:
        new_polygon=get_internal_first_polygon(polygon)
        bf_points=back_and_forth(new_polygon,spacing_list[i],separation,UAV_coords)
        bf_list.append(bf_points)
        i+=1

    return bf_list



"""
def plot_route(x,y,V,wpt_grid):
    x_plot=np.append(x,x[0])
    y_plot=np.append(y,y[0])

    plt.plot(x_plot, y_plot,'k*:')
    plt.scatter(wpt_grid[:,0],wpt_grid[:,1])
    plt.plot(wpt_grid[:,0],wpt_grid[:,1])
    plt.scatter(V[:,0],V[:,1])
    plt.draw()
"""   


def generate_waypoints3(UAV,V,assets,track_number_matrix,track_first,track_last):
    UAVnumber=len(UAV)
    waypoint_number=len(V)
    waypoint_mat=np.ones((UAVnumber,waypoint_number,2))*float("NaN")
    waypoint_mat_final=np.ones((UAVnumber,waypoint_number,2))*float("NaN")
    #First waypoint is UAV initial position (altitude change)

    #print(V)
    #print (V_points)

    count=1

    
    new_track=0
    aux_start=0

    for i,track in enumerate(track_number_matrix):
        
        aux_it=int(new_track+track+1)
        
        for j in range (int(aux_start), aux_it):
            waypoint_mat[i,int(j-aux_start),:]=V[j,:]

                    
        new_track=new_track+track
        aux_start=new_track+1
            
    #print(waypoint_mat)




    for i in range (0,UAVnumber):
        waypoint_mat_final[i,:,:]=waypoint_mat[assets[i], :,:]

    return waypoint_mat_final





def draw_all (waypoint_matrix,UAV,wpts):
    
    #plot_map()
    plt.scatter(UAV[:,0],UAV[:,1])
    plt.scatter(wpts[:,0],wpts[:,1])

    dx=0.2
    dy=0.2

    final_waypoint_matrix=np.ones((len(waypoint_matrix),len(waypoint_matrix[0])+2,2))*float("NaN")
    for i in range(0,len(UAV)):                 #add first waypoint
        final_waypoint_matrix[i,0,:]=UAV[i,:]

    for i in range(0,len(UAV)):    #add next and last waypoint
        for j in range (0, len(waypoint_matrix[0])):
            if not np.isnan(waypoint_matrix[i, j, 1]):
                final_waypoint_matrix[i,j+1,:]=waypoint_matrix[i,j,:]
                final_waypoint_matrix[i,j+2,:]=UAV[i,:]

    for i in range(0,len(UAV)):
        plt.plot(final_waypoint_matrix[i,:,0],final_waypoint_matrix[i,:,1])



 #   for i in range(0,len(UAV)):
 #           plt.plot(waypoint_matrix[i,:,0],waypoint_matrix[i,:,1])


    plt.draw()
    plt.show()




def write_mission_waypoints(waypoint_matrix, UAV_ini_coords,mission_altitude):
    last_item_lat=0.0
    last_item_lon=0.0
    for i in range (0,len(waypoint_matrix)):
        file_name=("wpt_file_%d.csv"%(i))
        file1 = open(file_name,"w+")
        file1.write("%f,%f,0\n"%(UAV_ini_coords[i,0], UAV_ini_coords[i,1])) #starting point
        file1.write("%f,%f,%d\n"%(UAV_ini_coords[i,0], UAV_ini_coords[i,1],mission_altitude)) #initial altitude

        for j in range (0,len(waypoint_matrix[0])):
            if not np.isnan(waypoint_matrix[i, j, 0]):
                file1.write("%f,%f,%d\n" %(waypoint_matrix[i,j,0], waypoint_matrix[i,j,1], mission_altitude))  
        file1.write("%f,%f,%d\n"%(UAV_ini_coords[i,0], UAV_ini_coords[i,1],mission_altitude)) #initial altitude
        file1.write("%f,%f,0\n"%(UAV_ini_coords[i,0], UAV_ini_coords[i,1])) #starting point




