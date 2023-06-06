import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

# [currentstate, testinginput]: nextstate
# dictionarytime = {[0, 0]: 1, [1, 0]: 0, [2, 0]: 0, [0, 1]: 2, [1, 1]: 2, [2, 1]: 1}

# edgelist = [(0, 1, color = 'red'), (2, 0, color = 'red'), (1, 2, color = 'red')]
# H = nx.Graph(edgelist)
# H.add_node(0, color = 'red')
# H.add_node(1, color = 'yellow')
# H.add_node(2, color = 'blue')

edgelist = [(0, 1, {'color': 'red'}), (2, 0, {'color': 'yellow'}), (1, 2, {'color': 'blue'})]
H = nx.DiGraph(edgelist)
print(H.edges)
# H.add_edge()

# H.add_edges_from(edgelist)

# node_color = 'g'
# edge_color = 'b'
nx.draw(H, with_labels=True)
plt.show()
