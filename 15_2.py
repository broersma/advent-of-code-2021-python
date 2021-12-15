import little_helper
import networkx as nx

input = list(list(int(level) for level in list(line)) for line in little_helper.get_input(15, 2021).split("\n"))

G = nx.DiGraph()

orig_max_y = len(input)
orig_max_x = len(input[0])

max_y = orig_max_y * 5
max_x = orig_max_x * 5

def risk(x,y):
    return (input[y%orig_max_y][x%orig_max_x] + y // orig_max_y + x // orig_max_x - 1) % 9 + 1

for y in range(max_y):
    for x in range(max_x):
        for (dx,dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
            if 0 <= x+dx < max_x and 0 <= y+dy < max_y:
                G.add_edge((x,y), (x+dx, y+dy), weight=risk(x,y))

print(sum(risk(x,y) for (x,y) in nx.shortest_path(G, source=(0,0), target=(max_x-1, max_y-1), weight='weight')[1:]))
