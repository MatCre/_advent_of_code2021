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


