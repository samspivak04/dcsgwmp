# import packages
import matplotlib.pyplot as plt
import networkx as nx
import copy


# edge labels dictionary
def edgelabelsfunction(H):
    edgelabelsdict = {}
    for nodestuple in H.edges():
        (firstnode, secondnode) = nodestuple  # unpack nodestuple
        edgelabelsdict[nodestuple] = str(firstnode) + " to " + str(secondnode)  # create labels and...
        # add them to edge labels dictionary
    return edgelabelsdict
def unreachablenodescolors(H):
    unreachablenodes = list(nx.isolates(H))  # make a list of the unreachable nodes
    nodecolors = []  # make a list of the colors for all the nodes
    for node in H.nodes():
        if node in unreachablenodes:
            nodecolors.append('green')  # make all unreachable nodes green
        else:
            nodecolors.append('tab:blue')  # make all reachable nodes blue
    return nodecolors

fileobject = open('path_data_weird_state_transitions.csv', 'w', encoding="utf-8")
fileobject.write("probability")
fileobject.write(",# original unreachable nodes")
fileobject.write(",,# previously unreachable nodes now reachable\n")

numberofnodes = 13
criticaledgeprobability = 1 / (numberofnodes - 1)


for probabilitydenominator in range(1, int(numberofnodes * 2)):  # create more accurate range
    fileobject.write(str(1 / probabilitydenominator))
    if probabilitydenominator == numberofnodes - 1:
        fileobject.write(" critical edge probability reached! 1 / " + str(probabilitydenominator))
    if round((1 / int(probabilitydenominator)), 2) == 0:
        fileobject.write("probability of connectivity too low. probability 1 / " + str(probabilitydenominator) + "\n")
        raise Exception("probability of connectivity too low. probability 1 / " + str(probabilitydenominator) + "\n")

    # generate erdos renyi graph
    H = nx.erdos_renyi_graph(numberofnodes, (1 / int(probabilitydenominator)), seed=5, directed=True)
    # J = copy.deepcopy(H)
    J = nx.erdos_renyi_graph(numberofnodes, (1/20), seed=5, directed=True)
    K = copy.deepcopy(H)
    K.add_edges_from([e for e in J.edges])
    # J.add_edges_from([e for e in S.edges])

    edgelabelsdictH = edgelabelsfunction(H)
    edgelabelsdictJ = edgelabelsfunction(J)

    unreachablenodescolorsH = unreachablenodescolors(H)
    unreachablenodesH = len(list(nx.isolates(H)))
    unreachablenodesK = len(list(nx.isolates(H))) - len(list(nx.isolates(K)))
    fileobject.write("," + str(unreachablenodesH))
    fileobject.write(",," + str(unreachablenodesK) + "\n")

    # # method='bellman-ford'
    # try:
    #     pathlist = nx.shortest_path(H, source=0, target=1, weight=None)
    # except nx.NetworkXNoPath:
    #     print("new edge will be created then deleted")
    #     fileobject.write("new edge will be created then deleted\n")
    #     H.add_edge(0, 1)
    #     print("The path from " + str(0) + " to " + str(1) + " is:")
    #     fileobject.write("The path from " + str(0) + " to " + str(1) + " is:" + "\n")
    #     for k in range(len(pathlist)):
    #         if k + 1 != len(set(pathlist)):
    #             print(str(pathlist[k]) + " to " + str(pathlist[k + 1]))
    #             fileobject.write(str(pathlist[k]) + " to " + str(pathlist[k + 1]) + "\n")
    #     H.remove_edge(int(0), int(1))
    # else:
    #     print("The path from " + str(0) + " to " + str(1) + " is:")
    #     fileobject.write("The path from " + str(0) + " to " + str(1) + " is:" + "\n")
    #     for k in range(len(pathlist)):
    #         if k + 1 != len(set(pathlist)):
    #             print(str(pathlist[k]) + " to " + str(pathlist[k + 1]))
    #             fileobject.write(str(pathlist[k]) + " to " + str(pathlist[k + 1]) + "\n")

    # path = dict(nx.all_pairs_shortest_path(H))
    # print(path)

    # display everything
    pos = nx.spring_layout(H)
    nx.draw(J, pos=pos, with_labels=True, node_color=unreachablenodescolorsH, edge_color="tab:blue")
    nx.draw_networkx_edge_labels(J, pos=pos, edge_labels=edgelabelsdictH, label_pos=0.5, font_weight='bold')
    nx.draw(H, pos=pos, with_labels=True, node_color=unreachablenodescolorsH)
    nx.draw_networkx_edge_labels(H, pos=pos, edge_labels=edgelabelsdictH, label_pos=0.5, font_weight='bold')

    plt.savefig("graph_weird_state_transitions_1over" + str(probabilitydenominator) + ".png")
    plt.show()

fileobject.close()
