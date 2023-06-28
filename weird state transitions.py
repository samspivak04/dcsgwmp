# import packages
import matplotlib.pyplot as plt
import networkx as nx

fileobject = open('path_data_weird_state_transitions.csv', 'w', encoding="utf-8")

numberofnodes = 50
criticaledgeprobability = 1 / (numberofnodes - 1)


for probabilitydenominator in range(1, int(numberofnodes)): # create more accurate range
    fileobject.write("starting with probability 1 / " + str(probabilitydenominator) + "\n")
    if probabilitydenominator == numberofnodes - 1:
        fileobject.write("critical edge probability reached! probability 1 / " + str(probabilitydenominator) + "\n")
    if round((1 / int(probabilitydenominator)), 2) == 0:
        fileobject.write("probability of connectivity too low. probability 1 / " + str(probabilitydenominator) + "\n")
        break

    # generate erdos renyi graph
    H = nx.erdos_renyi_graph(numberofnodes, (1 / int(probabilitydenominator)), seed=5, directed=True)

    # edge labels dictionary
    edgelabelsdict = {}
    for nodestuple in H.edges():
        (firstnode, secondnode) = nodestuple # unpack nodestuple
        edgelabelsdict[nodestuple] = str(firstnode) + " to " + str(secondnode) # create labels and...
        # add them to edge labels dictionary

    # display everything
    pos = nx.spring_layout(H)
    nx.draw(H, pos = pos, with_labels=True)
    nx.draw_networkx_edge_labels(H, pos = pos, edge_labels=edgelabelsdict, label_pos = 0.5, font_weight = 'bold')
    plt.savefig("graph_weird_state_transitions_1over" + str(probabilitydenominator) + ".png")
    plt.show()

fileobject.close()
