# i was originally going to experiment with finding if certain nodes are adjacent to each other on this file...
# i will figure this out eventually. right now, this program generates circle-shaped closed loops using a certain number
# of nodes (states) input by the user.


import matplotlib.pyplot as plt
import networkx as nx
# G = nx.Graph()

# [currentstate, testinginput]: nextstate
# dictionarytime = {[0, 0]: 1, [1, 0]: 0, [2, 0]: 0, [0, 1]: 2, [1, 1]: 2, [2, 1]: 1}

# edgelist = [(0, 1, color = 'red'), (2, 0, color = 'red'), (1, 2, color = 'red')]
# H = nx.Graph(edgelist)
# H.add_node(0, color = 'red')
# H.add_node(1, color = 'yellow')
# H.add_node(2, color = 'blue')

r = input("How many states would you like? There will be a 0th state. \n")
# v = int(r) + 1
# if type(r) == int:
#     v = int(r) + 1
# else:
#     TypeError

nodenumberslist = []
for i in range(0, int(r)):
    nodenumberslist.append(i)

newedgelist = []
edgelabelsdictionary = {}
z = len(set(nodenumberslist)) - 1
a = nodenumberslist[z]
b = nodenumberslist[0]
tuple2 = (a, b)
newedgelist.append(tuple2)
# tuple3 = a, "to", b
string1 = str(a) + " to " + str(b)
# tuple4 = tuple2: tuple3
edgelabelsdictionary[tuple2] = string1
for h in range(len(nodenumberslist)):
    if h + 1 != len(nodenumberslist):
        q = nodenumberslist[h]
        u = nodenumberslist[h + 1]
        tuple1 = (q, u)
        newedgelist.append(tuple1)
        # tuple5 = q, "to", u
        string2 = str(q) + " to " + str(u)
        edgelabelsdictionary[tuple1] = string2

H = nx.DiGraph(newedgelist)

# edgelist = [(0, 1, {'color': 'red'}), (2, 0, {'color': 'yellow'}), (1, 2, {'color': 'blue'})]
# H = nx.DiGraph(edgelist)
# print(H.edges)
# H.add_edge()

# H.add_edges_from(edgelist)

# node_color = 'g'
# edge_color = 'b'

# print(H.adjacency())

pos = nx.spring_layout(H)
nx.draw(H, pos = pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos = pos, edge_labels = edgelabelsdictionary, label_pos = 0.5, font_weight = 'bold')
plt.show()
