'''Calculate the amount of times lines cross on a battleship esque board'''

import re
import pprint
import numpy

data = []

line_data = []

def coords_between_points(x,y):
    x = int(x)
    y = int(y)
    if x < y:
        return [i for i in range(x,y+1)]
    elif x > y:
        return [i for i in range(x, y-1, -1)]

def coord_between_points_diagonal(start_x,end_x,start_y,end_y):
    start_x = int(start_x)
    end_x = int(end_x)
    start_y = int(start_y)
    end_y = int(end_y)
    x_points = []
    y_points = []
    print(f"From {start_x, start_y} to {end_x, end_y}")

    if start_x < end_x:
        for i in range(0,end_x - start_x + 1):
            x_points.append(start_x + i)
    elif start_x > end_x:
        for i in range(0,start_x - end_x + 1):
            x_points.append(start_x - i)
    
    if start_y < end_y:
        for i in range(0,end_y - start_y + 1):
            y_points.append(start_y + i)
    elif start_y > end_y:
        for i in range(0,start_y - end_y + 1):
            y_points.append(start_y - i)
    combined = []
    for i in range(len(x_points)):
        combined.append((x_points[i],y_points[i]))

    return combined
        


pattern = r"(\d,\d) -> (\d,\d)"
with open("./05/data.txt", "r") as file:
    lines = file.readlines()
    for l in lines:
        results = re.match(pattern, l)
        line_start = results.group(1)
        line_end = results.group(2)
        line_coords = (line_start,line_end)
        line_data.append(line_coords)

grid = {tuple(str(i).zfill(2)):0 for i in range(100)}

for lines in line_data:
    start_x = lines[0][0]
    start_y = lines[0][2]
    end_x = lines[1][0]
    end_y = lines[1][2]

    print(f"Line starts at {start_x}, {start_y} and goes to {end_x}, {end_y}")
    if start_y == end_y:
        coords = coords_between_points(start_x,end_x)
        print("Vertical Line")
        for key,i in enumerate(coords):
            coords[key] = tuple((i,start_y))
        print(coords)
    elif start_x == end_x:
        coords = coords_between_points(start_y, end_y)
        print("Horizontal Line")
        print(coords)
        for key,i in enumerate(coords):
            coords[key] = tuple((start_x, i))
        print(coords)
    else:
        print("Diagonal Line")
        coords = coord_between_points_diagonal(start_x,end_x, start_y,end_y)
        print(coords)
        #For diagonal lines increment / decrement betwwen start x and end x and start y and end y 8,0 0,8 -> 7,1 6,2 5,3 4,4 3,5 2,6 1,7 0,8


