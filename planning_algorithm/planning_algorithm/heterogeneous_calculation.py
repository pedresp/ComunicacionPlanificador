##  Operaciones con robots heterogeneos #
##  Autor: Marco Luna                   #


import numpy as np
from numpy import linalg as LA
from scipy.optimize import linear_sum_assignment



#def get_score(UAV_list, UAV_area):

def get_score(total_area, scan_width, velocity, remaining_batt_time):
    scan_velocity=scan_width*velocity
    scan_time=total_area/scan_velocity
    score=remaining_batt_time/(scan_time)
    return score


def get_UAV_score_list(UAV, total_area):
    score_list=[]
    for features in UAV:
        score=get_score(total_area, features[2], features[3], features[4])
        score_list.append(score)
        #print(score)

    normalized_score=normalize_values(score_list)
    return normalized_score



def bin_pack_alg(track_weights,bin_weights):
    track_number=len(track_weights)
    bin_number=len(bin_weights)
    
    bins=np.zeros((bin_number,track_number))
    index_mat=np.ones((bin_number,track_number))*-1
    weight_sum_mat=np.zeros((bin_number))

    count=0
    weight_sum=0

    V_bin_max=bin_weights[count]
    previous_add_result=V_bin_max
    for item,weight in enumerate(track_weights):
        new_weight_sum=weight+weight_sum  #Aqui sumamos el peso al anadir una nueva pista a la lista del UAV
        current_add_result=abs(V_bin_max-new_weight_sum) #El valor que me falta o sobra al anadir la pista 

        if  current_add_result>previous_add_result: #Evaluar si al anadir la nueva pista estamos mas lejos que al anadir la anterior
            count=count+1
            if count>bin_number-1:
                count=bin_number-1
            V_bin_max=bin_weights[count]
            new_weight_sum=weight #actualizar el valor de new weight sum

        bins[count,item]=weight
        index_mat[count,item]=item
        weight_sum_mat[count]=sum(bins[count,:])

        weight_sum=new_weight_sum
        previous_add_result=abs(V_bin_max-new_weight_sum)

    return index_mat,weight_sum_mat



def track_asset(tracks_ini,UAV_ini,UAV_ini_weights):
    numberoftracks=len(tracks_ini)-1
    UAVnumber=len(UAV_ini)
    C=np.zeros((UAVnumber,numberoftracks))
    dist_mat=np.zeros((numberoftracks))
    UAV_weights=np.zeros((UAVnumber))
    
    tracks=np.array(tracks_ini)
    UAV=np.array(UAV_ini)
   #flow_matrix
    for i in range(0,numberoftracks):
        dist_mat[i]=LA.norm(tracks[i,:]-tracks[i+1,:])
        
    for i in range(0,UAVnumber):
        UAV_weights[i]=UAV_ini_weights[i]*sum(dist_mat)    

   
    track_asset,track_dist_mat=bin_pack_alg(dist_mat,UAV_weights)
    
    
    
    track_firsts=np.zeros((UAVnumber))
    track_lasts=np.zeros((UAVnumber))
    individual_track_number=np.zeros((UAVnumber))
    
    for i in range (0,UAVnumber):
        iterator = filter(lambda x: (x>=0), track_asset[i,:]) 
        filtered=list(iterator)
        individual_track_number[i]=len(filtered) #Numero de pistas
        if individual_track_number[i]>0:
            track_firsts[i]=min(filtered)
            track_lasts[i]=max(filtered)
    
    
    cost=np.zeros((UAVnumber))
    asset_col=[]
    #print (track_dist_mat)
    
    
    for i in range (0,UAVnumber):
    
        asset_col.append(i)
        arrive_cost=abs(LA.norm(tracks[int(track_firsts[i]),:]-UAV[i,:]))
        return_cost=abs(LA.norm(tracks[int(track_lasts[i]),:]-UAV[i,:]))
        mission_cost=abs(track_dist_mat[i])
        cost[i]=mission_cost#+arrive_cost+return_cost
    
    
    
     
    
    asset=np.array(asset_col)
    
    return asset,individual_track_number,cost





def get_norm(UAV_list):
    norm_list=[]
    for vector in UAV_list:
        norm_list.append(LA.norm(vector))
    
    normalized_vector=normalize_values(norm_list)
    return normalized_vector


def normalize_values(values):

    val_sum= sum(values)
    normalized_list=[]

    for val in values:
        normalized_list.append(val/val_sum)
    
    return normalized_list



def classify_by_scan(main_UAV_list, scores):

  # Crear un diccionario donde la clave es el primer valor del vector y el valor es una lista de vectores con ese valor.
    dict = {}
    w_list={}
    for i, UAV in enumerate(main_UAV_list):
        UAV_number=i
        scan_val = UAV[2] #El tamaño del scan se guarda en el valor 2

        if scan_val not in dict: #si no existe el valor, se agrega al diccionario
            dict[scan_val] = [] #crear lista vacía
            w_list[scan_val]=[]
        info=[UAV_number,scores[i]]   
        dict[scan_val].append(info)


  # Devolver el primer diccionario y la lista de listas.
    return dict

def check_sum_of_elements(weight_list):
#Comprueba que la suma de los elementos de un vector sea igual a 1
    # Utiliza una comprensión de lista para obtener los segundos elementos
    weights=[weight[1] for weight in weight_list]
    sum_of_elements=sum(weights)

    if sum_of_elements != 1:
        difference = 1 - sum_of_elements
        last= weight_list[-1]
        last[1]+= difference
        

    return weight_list



def get_area_weights(score_dict):

    weigths_list=[]

    for key, score_list in score_dict.items():
        score_sum=sum(scores for _, scores in score_list)
        vector=[key, score_sum]
        weigths_list.append(vector)

    weights_filtered=check_sum_of_elements(weigths_list)


    return  weights_filtered



def get_distance_based_weights_and_coords(UAV_list):
    
    max_distance_list=[]
    coords=[]

    for UAV in UAV_list:
        x=UAV[0]
        y=UAV[1]
        coords.append([x,y])
        velocity=UAV[3]
        time_remaining=UAV[4]
        max_distance=velocity*time_remaining
        max_distance_list.append(max_distance)
    
    normalized_weights=normalize_values(max_distance_list)

    return normalized_weights,coords
    


def get_weight_and_coord_list(UAV_list,scan_dict):
    
    weight_list=[]
    coord_list=[]
    for key in scan_dict:
        value=scan_dict[key]
        current_UAV_list=[]
        for element in value:
            current_UAV=UAV_list[element[0]]
            current_UAV_list.append(current_UAV) #tengo los drones de cada scan
        
        
        weights, coords=get_distance_based_weights_and_coords(current_UAV_list) #Hasta aquí pesos y coordenadas

        weight_list.append(weights)
        coord_list.append(coords)
            
      

    
    
    return weight_list,coord_list
    


def generate_waypoints(UAV,V_ini,assets,track_number_matrix):
    UAVnumber=len(UAV)
    waypoint_number=len(V_ini)
    waypoint_mat=np.ones((UAVnumber,waypoint_number,2))*float("NaN")
    waypoint_mat_final=np.ones((UAVnumber,waypoint_number,2))*float("NaN")
    #First waypoint is UAV initial position (altitude change)

    #print(V)
    #print (V_points)
    V=np.array(V_ini)
    assets=np.array(assets)

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







def final_assingment(weight_list, coords_list, bf_list):

    i=0

    cost_list=[]
    waypoints_list=[]
    
    for track in bf_list:
        assets,track_number,cost=track_asset(track,coords_list[i],weight_list[i])
        waypoints=generate_waypoints(coords_list[i],track,assets,track_number) #Relative waypoints
        waypoints_list.append(waypoints)
        cost_list.append(cost)
        i=i+1
    
    return waypoints_list, cost_list






