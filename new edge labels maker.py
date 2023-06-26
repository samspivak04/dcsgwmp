import matplotlib.pyplot as plt
import networkx as nx

H = nx.erdos_renyi_graph(50, (1 / 49), seed=5, directed=True)
newdict = {}
for nodestuple in H.edges():
    (firstnode, secondnode) = nodestuple
    newdict[nodestuple] = str(firstnode) + " to " + str(secondnode)
print(newdict)
pos = nx.spring_layout(H)
nx.draw(H, pos = pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos = pos, edge_labels=newdict, label_pos = 0.5, font_weight = 'bold')
plt.show()