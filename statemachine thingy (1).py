from statemachine import StateMachine, State

# import packages
import matplotlib.pyplot as plt
import networkx as nx

fileobject = open('path_data_statemachine_thingy_(1)', 'w', encoding="utf-8")

numberofnodes = 11
criticaledgeprobability = 1 / (numberofnodes - 1)


# for probabilitydenominator in range(1, int(numberofnodes * 2)):  # create more accurate range
#     fileobject.write("starting with probability 1 / " + str(probabilitydenominator) + "\n")
#     if probabilitydenominator == numberofnodes - 1:
#         fileobject.write("critical edge probability reached! probability 1 / " + str(probabilitydenominator) + "\n")
#     if round((1 / int(probabilitydenominator)), 2) == 0:
#         fileobject.write("probability of connectivity too low. probability 1 / " + str(probabilitydenominator) + "\n")
#         raise Exception("probability of connectivity too low. probability 1 / " + str(probabilitydenominator) + "\n")

# generate erdos renyi graph
H = nx.erdos_renyi_graph(numberofnodes, criticaledgeprobability, seed=5, directed=True)

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
plt.savefig("graph_statemachine_thingy_(1)_" + str(criticaledgeprobability) + ".png")
plt.show()

fileobject.close()


class TrafficLightMachine(StateMachine):
    """StateMachine is SM"""

    n0 = State(initial=True)
    n1 = State()
    n2 = State()
    n3 = State()
    n4 = State()
    n5 = State()
    n6 = State()
    n7 = State()
    n8 = State()
    n9 = State()
    n10 = State()


    # nodesdict = {}
    # for node in H.nodes:
    #     # nodesdict["node" + str(node)] = node
    #     nodesdict[node] = ("node" + str(node))
    # stateslist = []
    # for key, value in nodesdict.items():
    #     value = State()
    #     stateslist.append(value)
    # for entry in stateslist:
    #     print(type(entry))

    # green = State(initial=True)
    # yellow = State()
    # red = State()

    # range(len(list(H.edges)))
    # for nodestupleSM in H.edges:
    #     (firstnodeSM, secondnodeSM) = nodestupleSM
    #     precondition = nodesdict[firstnodeSM]
    #     postcondition = nodesdict[secondnodeSM]
    #     # precondition = "node" + str(firstnodeSM)
    #     # postcondition = "node" + str(secondnodeSM)
    #     move = (
    #         precondition.to(postcondition)
    #     )

    move = (
        n0.to(n1)
        | n1.to(n2)
        | n2.to(n3)
        | n3.to(n4)
        | n4.to(n5)
        | n5.to(n6)
        | n6.to(n7)
        | n7.to(n8)
        | n8.to(n9)
        | n9.to(n10)
        | n10.to(n0)
    )

    # cycle = (
    #     green.to(yellow)
    #     | yellow.to(red)
    #     | red.to(green)
    # )

    def before_move(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"{event} from {source.id} to {target.id}{message}"

    def on_enter_red(self):
        print("Don't move.")

    def on_exit_red(self):
        print("Go ahead!")


test = TrafficLightMachine()
print(test.send("move"))
print(test.current_state.id)
