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
            new_array_3d.append(new_array_2d)
        new_wps.append(new_array_3d)
    
    return new_wps
