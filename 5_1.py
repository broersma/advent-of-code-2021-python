import little_helper
from collections import defaultdict

input = little_helper.get_input(5, 2021).split("\n")
input = (tuple(tuple(int(coordinate) for coordinate in component.split(",")) for component in line.split(" -> ")) for line in input)

diagram = defaultdict(int)

for line in input:
    if line[0][0] == line[1][0]:
        x = line[0][0]
        ymin = min(line[0][1], line[1][1])
        ymax = max(line[0][1], line[1][1])
        for y in range(ymin, ymax + 1):
            diagram[(x, y)] += 1
    elif line[0][1] == line[1][1]:
        y = line[0][1]
        xmin = min(line[0][0], line[1][0])
        xmax = max(line[0][0], line[1][0])
        for x in range(xmin, xmax + 1):
            diagram[(x, y)] += 1

print(len([value for value in diagram.values() if value > 1]))
