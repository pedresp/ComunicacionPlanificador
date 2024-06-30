class InsufficientBattery(Exception):
    def __init__(self, message=""):
        super().__init__(message)

class WrongEstimationSelected(Exception):
    def __init__(self, message=""):
        super().__init__(message)


def TFC_distance_calculation(coord, polygon):
    three_distances = [0, 0, 0] #the three greatest difference between coord and other points abs(coord - coord_point)
  
    distance = 0
    for coord_point in polygon:
        distance = abs(coord - coord_point) 
     
        i = 0
        while i < 3 and distance > three_distances[i]: i += 1
  
        if i > 0:
            three_distances.insert(i, distance)
            three_distances.pop(0)
  
    return sum(three_distances)/3

def centroid_calculation(vertex):
    n = len(vertex)
    
    # get polygon area using Gauss 
    area = 0.0
    for i in range(n):
        x1, y1 = vertex[i]
        x2, y2 = vertex[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    area = abs(area) / 2.0

    # calculate polygon coordinates 
    C_x = 0.0
    C_y = 0.0
    for i in range(n):
        x1, y1 = vertex[i]
        x2, y2 = vertex[(i + 1) % n]
        factor = (x1 * y2 - x2 * y1)
        C_x += (x1 + x2) * factor
        C_y += (y1 + y2) * factor
    
    C_x /= (6.0 * area)
    C_y /= (6.0 * area)

    return (C_x, C_y)

def TFC_estimation(UAVs, polygon, height, is075=False):
    #dictionaries to avoid calculating estimates paths for equal x or y values
    distances_to_mission_x = {}
    distances_to_mission_y = {}
  
    polygon_x = [ coord[0] for coord in polygon ]
    polygon_y = [ coord[1] for coord in polygon ]
  
    #debugging
    dist = []
  
    for UAV in UAVs:
        x = UAV[0]
        if x not in distances_to_mission_x:
            distances_to_mission_x[x] = TFC_distance_calculation(x, polygon_x)
     
        y = UAV[1]
        if y not in distances_to_mission_y:
            distances_to_mission_y[y] = TFC_distance_calculation(y, polygon_y)
  
        multiplication_value = 2 if not is075 else 1.5

        candidate_batt = UAV[4] - multiplication_value*(pow(pow(distances_to_mission_x[x], 2)+pow(distances_to_mission_y[y], 2) + pow(height,2), 0.5))/UAV[3]
        UAV[4] = candidate_batt if candidate_batt > 0 else 0
  
        dist.append(multiplication_value*(pow(pow(distances_to_mission_x[x], 2)+pow(distances_to_mission_y[y], 2)+pow(height,2), 0.5)))
  
    return dist

def Centroid_estimation(UAVs, polygon, height):
    #centroid of the polygon
    centroid = centroid_calculation(polygon) 

    # debugging
    dist = []
    for UAV in UAVs:
        candidate_batt = UAV[4] - 2*(pow(pow(UAV[0]-centroid[0], 2) + pow(UAV[1]-centroid[1], 2) + pow(height, 2), 0.5))/UAV[3]               
        UAV[4] = candidate_batt if candidate_batt > 0 else 0

        dist.append(2*(pow(pow(UAV[0]-centroid[0], 2) + pow(UAV[1]-centroid[1], 2) + pow(height, 2), 0.5)))

    return dist

def execute_estimation(UAVs, polygon, height, method="TFC"):
    match(method):
        case "TFC":
            return TFC_estimation(UAVs, polygon, height, False)
        case "TFC075":
            return TFC_estimation(UAVs, polygon, height, True)
        case "centroid":
            return Centroid_estimation(UAVs, polygon, height)
        case _:
            raise WrongEstimationSelected(f"the estimation {method} is not supported")

if __name__ == '__main__':
  polygons = [[-139.85, 62.58 ], [-126.91, -47.81], [-66.26, -80.52], [42.77, -92.11], [100, -50], [140.89, 10.79], [129.31, 100.74], [61.85, 172.97], [-83.98, 194.09]]

  UAVs = [[-200.0, 0.0, 20.0, 20.0, 80.0], [-200.0, 0.0, 10.0, 15.0, 150.0], [-200.0, 0.0, 15.0, 15.0, 150.0]]
  estimate_new_battery(UAVs, polygons)

