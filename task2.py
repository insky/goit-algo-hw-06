import networkx as nx
from cities import cities_graph


def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

G = nx.Graph()
G.add_edges_from(
    (city, neighbor)
    for city, neighbors in cities_graph.items()
    for neighbor in neighbors
)

start_city = "Львів"
goal_city = "Херсон"

dfs_result = dfs_path(G, start_city, goal_city)
bfs_result = bfs_path(G, start_city, goal_city)

print("Результати пошуку:")
print(f"DFS: {dfs_result}")
print(f"BFS: {bfs_result}")
