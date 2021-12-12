from collections import defaultdict
import little_helper

input = list(list(int(level) for level in list(line)) for line in little_helper.get_input(9, 2021).split("\n"))

max_y = len(input)
max_x = len(input[0])
risk_level = 0
for y in range(max_y):
    for x in range(max_x):
        if all(input[y][x] < input[y-dy][x-dx] for (dx,dy) in [(0,-1),(-1, 0), (1,0), (0,1)] if 0 <= x-dx < max_x and 0 <= y-dy < max_y):
            risk_level += 1 + input[y][x]

print(risk_level)
