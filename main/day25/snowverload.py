import math

import matplotlib.pyplot as plt
import networkx as nx


def solve(graph) -> int:
    # visualise_graph(graph)  # use this to find the three connections and delete them from the input
    return get_cluster_sizes(graph)


def get_cluster_sizes(graph):
    subgraph_sizes = []
    cluster_size = {}
    for node in graph.keys():
        if node in cluster_size:
            continue
        subgraph = traverse_graph(node, graph)
        subgraph_sizes.append(len(subgraph))
        for child in traverse_graph(node, graph):
            cluster_size[child] = len(subgraph)
    return math.prod(v for v in subgraph_sizes)


def traverse_graph(node, graph):
    seen = set()
    to_visit = [node]
    while to_visit:
        current = to_visit.pop()
        if current in seen:
            continue
        seen.add(current)
        to_visit.extend(graph[current])
    return seen


def visualise_graph(graph):
    nx_graph = nx.DiGraph(graph)
    nx.draw(nx_graph, with_labels=True)
    plt.show()
