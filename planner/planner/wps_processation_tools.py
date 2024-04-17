import numpy as np

class Drone_initial:
    def __init__(self, name : str, coords : tuple[float, float]):
        self.name = name
        self.coords = coords
    
class WPS_metadata:
    def __init__(self) -> None:
        self.map_struct = {}
    
    def add_drone(self, drone : Drone_initial, sweep_width: float) -> None:
        try:
            self.map_struct[sweep_width].append(drone)
        except:
            self.map_struct[sweep_width] = []
            self.map_struct[sweep_width].append(drone)

    def flatten(self) -> list[Drone_initial]:
        result = []
        for data in self.map_struct.items():
            for elem in data[1]:
                result.append(elem)
        return result
    
    def flatten_str(self) -> list[str]:
        result = []
        for data in self.map_struct.items():
            for elem in data[1]:
                result.append(elem.name)
        return result        

def same_line(point0, point1, point2) -> bool:
    vector1 = (point1[0] - point0[0], point1[1] - point0[1], point1[2] - point0[2])
    vector2 = (point2[0] - point0[0], point2[1] - point0[1], point2[2] - point0[2])

    diff_x = vector1[1] * vector2[2] - vector1[2] * vector2[1]
    diff_y = vector1[2] * vector2[0] - vector1[0] * vector2[2]
    diff_z = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    if abs(diff_x) < 0.001 and abs(diff_y) < 0.001 and abs(diff_z) < 0.001:
        return True
    return False

def rm_intermediate_points(wps) -> list[np.array]:
    if (len(wps) < 3):
        return wps
    index = 2
    point0 = wps[0]
    point1 = wps[1]
    new_wps = [point0]
    while (index < len(wps)):
        point2 = wps[index]
        if not same_line(point0, point1, point2):
            new_wps.append(point1)
            point0 = point1
        point1 = point2
        index += 1
    new_wps.append(point2)
    return new_wps

def process_wps(array_list : list[np.array], z_value : float) -> list[np.array]:
    new_wps = []
    for array_3d in array_list:
        new_array_3d = []
        for array_2d in array_3d:
            new_array_2d = np.empty((0,3))
            for array_1d in array_2d:
                if not np.isnan(array_1d).any():
                    array_to_append = np.append(array_1d, [z_value], axis=0)
                    new_array_2d = np.append(new_array_2d, [array_to_append], axis=0)
            new_array_2d = rm_intermediate_points(new_array_2d)
            new_array_3d.append(new_array_2d)
        new_wps.append(new_array_3d)
    return new_wps