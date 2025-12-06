import networkx as nx
import matplotlib.pyplot as plt
from cities import cities_graph

G = nx.Graph()
G.add_edges_from(
    (city, neighbor)
    for city, neighbors in cities_graph.items()
    for neighbor in neighbors
)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for city, degree in degrees.items():
    print(f"  {city}: {degree}")

nx.draw(G, with_labels=True, font_family="Arial", font_size=10, node_color="lightblue", edge_color="gray")
plt.title("Граф міст України")
plt.show()
