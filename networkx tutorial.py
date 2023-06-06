import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_node(1)

G.add_edge(1, 2)
G.add_edge(1, 3)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*

G.add_node("sam")
G.add_nodes_from("dog")
G.add_edge(1, "s")
G.add_edge("a", "o")

x = G.number_of_nodes()
y = G.number_of_edges()
print(x)
print(y)

nx.draw(G)
plt.show()
