import little_helper
from collections import defaultdict
from itertools import zip_longest


def range2(a, b):
    if b > a:
        yield from range(a, b + 1)
    else:
        yield from range(a, b - 1, -1)


input = little_helper.get_input(5, 2021).split("\n")
input = (tuple(tuple(int(coordinate) for coordinate in component.split(",")) for component in line.split(" -> ")) for line in input)

diagram = defaultdict(int)

for line in input:
    xs = list(range2(line[0][0], line[1][0]))
    ys = list(range2(line[0][1], line[1][1]))

    for (x,y) in zip_longest(xs, ys, fillvalue=xs[0] if len(xs) == 1 else ys[0]):
        diagram[(x, y)] += 1

print(len([value for value in diagram.values() if value > 1]))
