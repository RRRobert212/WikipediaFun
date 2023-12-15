import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_size=8, node_size=50)
    plt.show()