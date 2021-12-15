import little_helper
import networkx as nx

input = list(list(int(level) for level in list(line)) for line in little_helper.get_input(15, 2021).split("\n"))

G = nx.DiGraph()

for y in range(len(input)):
    for x in range(len(input[0])):
        for (dx,dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
            if 0 <= x+dx < len(input[0]) and 0 <= y+dy < len(input):
                G.add_edge((x,y), (x+dx, y+dy), weight=input[y][x])

print(sum(input[y][x] for (x,y) in nx.shortest_path(G, source=(0,0), target=(len(input[0])-1, len(input)-1), weight='weight')[1:]))
