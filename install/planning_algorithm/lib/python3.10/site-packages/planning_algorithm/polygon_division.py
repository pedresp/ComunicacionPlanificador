
from pode import divide, Contour, Point, Polygon, Requirement, joined_constrained_delaunay_triangles
import numpy as np

def get_pode_parts(limits, weights):
    point_list=[]
    for points in limits:
        point_list.append(Point(points[0],points[1]))
    
    contour=Contour(point_list)
    polygon=Polygon(contour)

    requirements=[]
    for req in weights:
        requirements.append(Requirement(req))
    
    parts=divide(polygon,requirements,joined_constrained_delaunay_triangles)

    polygon_list=get_polygon_list_from_parts(parts)



    return polygon_list

    


def get_polygon_list_from_parts(parts):

    polygon_list=[]
    for polygons in parts:
        #print(polygons._border)
        area=[]
        border=polygons._border
        vertices=border.vertices
        for points in vertices:
            area.append([float(points._coordinates[0]),float(points._coordinates[1])])
        
        polygon_list.append(area)
    
    return polygon_list
    
    
    
        
        




 

"""
contour = Contour([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
polygon = Polygon(contour)
requirements = [Requirement(0.25), Requirement(0.25), Requirement(0.25), Requirement(0.25)]
parts = divide(polygon, requirements)

point=Point(0,0)
print(point._coordinates[0])
print(polygon.border)
print(contour.vertices)

for points in parts:
    print(points)

"""