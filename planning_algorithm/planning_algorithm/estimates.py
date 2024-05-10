class InsufficientBattery(Exception):
  def __init__(self, message=""):
    super().__init__(message)

def estimate_path(coord, polygon):
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

def estimate_new_battery(UAVs, polygon):
  #dictionaries to avoid calculating estimates paths for equal x or y values
  distances_to_mission_x = {}
  distances_to_mission_y = {}

  polygon_x = [ coord[0] for coord in polygon ]
  polygon_y = [ coord[1] for coord in polygon ]

  for UAV in UAVs:
   x = UAV[0]
   if x not in distances_to_mission_x:
     distances_to_mission_x[x] = estimate_path(x, polygon_x)
   
   y = UAV[1]
   if y not in distances_to_mission_y:
     distances_to_mission_y[y] = estimate_path(y, polygon_y)

   candidate_batt = UAV[4] - 2*(pow(pow(distances_to_mission_x[x], 2)+pow(distances_to_mission_y[y], 2), 0.5))/UAV[3]
   UAV[4] = candidate_batt if candidate_batt > 0 else 0

if __name__ == '__main__':
  polygons = [[-139.85, 62.58 ], [-126.91, -47.81], [-66.26, -80.52], [42.77, -92.11], [100, -50], [140.89, 10.79], [129.31, 100.74], [61.85, 172.97], [-83.98, 194.09]]

  UAVs = [[-200.0, 0.0, 20.0, 20.0, 80.0], [-200.0, 0.0, 10.0, 15.0, 150.0], [-200.0, 0.0, 15.0, 15.0, 150.0]]
  estimate_new_battery(UAVs, polygons)

