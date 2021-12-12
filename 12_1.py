import little_helper
import networkx as nx

input = list(tuple(line.split("-")) for line in little_helper.get_input(12, 2021).split("\n"))

G = nx.Graph()

G.add_edges_from(input)

def get_paths(G, start, end, visited = set()):
    if start == end:
        return [[end]]
    else:
        paths = []
        if start.islower():
            visited.add(start)
        for node in G.neighbors(start):
            if node not in visited:
                old_paths = get_paths(G, node, end, visited.copy())
                for old_path in old_paths:
                    paths.append([start] + old_path)
        return paths

print(len(get_paths(G, "start", "end")))
