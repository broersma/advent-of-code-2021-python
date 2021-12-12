from functools import reduce
import operator
import little_helper

input = list(list(int(level) for level in list(line)) for line in little_helper.get_input(9, 2021).split("\n"))

max_y = len(input)
max_x = len(input[0])

low_points = set()

for y in range(max_y):
    for x in range(max_x):
        if all(input[y][x] < input[y-dy][x-dx] for (dx,dy) in [(0,-1),(-1, 0), (1,0), (0,1)] if 0 <= x-dx < max_x and 0 <= y-dy < max_y):
            low_points.add((x,y))

basins = {}

for low_point in low_points:
    points = set([low_point])

    points_added = True
    while points_added:
        new_neighbors = set()
        for (x,y) in points:
            neighbors = set((x + dx, y + dy) for (dx,dy) in [(0,-1),(-1, 0), (1,0), (0,1)] if 0 <= x+dx < max_x and 0 <= y+dy < max_y and input[y+dy][x+dx] < 9 and (x + dx, y + dy) not in points)
            new_neighbors |= neighbors
        if len(new_neighbors) == 0:
           break
        else:
            points |= new_neighbors

    basins[low_point] = len(points)

print(reduce(operator.__mul__, (basins[k] for k in sorted(basins, key=lambda k: basins[k], reverse=True)[:3])))
