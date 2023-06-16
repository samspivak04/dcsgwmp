import matplotlib.pyplot as plt
import networkx as nx

fileobject = open('path_data.txt', 'w', encoding="utf-8")

# G = nx.Graph()

# [currentstate, testinginput]: nextstate
# dictionarytime = {[0, 0]: 1, [1, 0]: 0, [2, 0]: 0, [0, 1]: 2, [1, 1]: 2, [2, 1]: 1}

# edgelist = [(0, 1, color = 'red'), (2, 0, color = 'red'), (1, 2, color = 'red')]
# H = nx.Graph(edgelist)
# H.add_node(0, color = 'red')
# H.add_node(1, color = 'yellow')
# H.add_node(2, color = 'blue')

r = 20

for p in range(1, int(r)):
    fileobject.write("starting with probability 1 / " + str(p) + "\n")




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

    H = nx.erdos_renyi_graph(int(r), (1 / int(p)), seed=5, directed=True)
    # H = nx.DiGraph(newedgelist)

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
    plt.savefig("graph_" + str(p) + ".png")
    plt.show()


    e = int(r) - 1
    l = 0
    j = 1
    # method='bellman-ford'
    try:
        pathlist = nx.shortest_path(H, source=int(l), target=int(j), weight=None)
    except nx.NetworkXNoPath:
        print("new edge will be created then deleted")
        fileobject.write("new edge will be created then deleted\n")
        H.add_edge(int(l), int(j))
        print("The path from " + str(l) + " to " + str(j) + " is:")
        for k in range(len(pathlist)):
            if k + 1 != len(set(pathlist)):
                print(str(pathlist[k]) + " to " + str(pathlist[k + 1]))
        H.remove_edge(int(l), int(j))
    else:
        print("The path from " + str(l) + " to " + str(j) + " is:")
        for k in range(len(pathlist)):
            if k + 1 != len(set(pathlist)):
                print(str(pathlist[k]) + " to " + str(pathlist[k + 1]))

# when "raise nx.NetworkXNoPath(f"No path between {source} and {target}.")"...
# networkx.exception.NetworkXNoPath: No path between 3 and 2." ...
# create new node & edge to reach target. maybe helpful to create base class and make the weird aspect a file...
# imported by the class?

# make sure new node and target do not display (weird aspect)
#
fileobject.close()