import networkx as nx
import matplotlib.pyplot as plt
from cities import cities_graph


def dijkstra(graph, start_node):
    return nx.single_source_dijkstra_path_length(graph, start_node)


G = nx.Graph()
G.add_edges_from(
    (city, neighbor, {"weight": weight})
    for city, neighbors in cities_graph.items()
    for neighbor, weight in neighbors.items()
)
edge_labels = nx.get_edge_attributes(G, 'weight')

start_city = "Київ"
shortest_paths = dijkstra(G, start_city)
print(f"Найкоротші шляхи від {start_city}:")
for city, distance in shortest_paths.items():
    if distance > 0:
        print(f"  До {city}: {distance} км")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_family="Arial", font_size=10, node_color="lightblue", edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="green", font_size=8)
plt.title(f"Граф міст України з вагами ребер (відстані в км)")
plt.show()
