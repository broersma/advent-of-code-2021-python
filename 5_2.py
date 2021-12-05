import little_helper
from collections import defaultdict
from itertools import zip_longest

input = little_helper.get_input(5, 2021).split("\n")
input = (tuple(tuple(int(coordinate) for coordinate in component.split(",")) for component in line.split(" -> ")) for line in input)

diagram = defaultdict(int)

for line in input:
    xmin = min(line[0][0], line[1][0])
    xmax = max(line[0][0], line[1][0])
    ymin = min(line[0][1], line[1][1])
    ymax = max(line[0][1], line[1][1])
    
    stepx = -1 if line[0][0] > line[1][0] else 1
    xs = range(line[0][0], line[1][0] + stepx, stepx)

    stepy =-1 if line[0][1] > line[1][1] else 1
    ys = range(line[0][1], line[1][1] + stepy, stepy)

    for (x,y) in zip_longest(xs, ys, fillvalue=xmin if xmin==xmax else ymin):
        diagram[(x, y)] += 1

print(len([value for value in diagram.values() if value > 1]))
