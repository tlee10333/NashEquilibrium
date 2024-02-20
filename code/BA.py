import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
from typing import *
from networkx.algorithms.approximation import average_clustering
from utils import decorate, savefig

import random



#Written By Allan Downey
def barabasi_albert_graph(num_nodes: int, num_edges_per_node: int,
                          seed: Optional[int] = None):
    """
    Construct a Barabasi-Albert graph.

    Args:
      num_nodes: an int, the number of nodes in the resulting graph
      num_edges_per_node: an int, the number of edges each new node gets
      seed: an int, a random seed for testing purposes, or None to not set

    Returns:
      a nx.Graph representing a Barabasi Albert graph with the given parameters
    """
    if seed is not None:
        random.seed(seed)

    G = nx.empty_graph(num_edges_per_node)
    targets = set(range(num_edges_per_node))
    repeated_nodes = []

    for source in range(num_edges_per_node, num_nodes):

        G.add_edges_from(zip([source]*num_edges_per_node, targets))

        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * num_edges_per_node)

        targets = random_subset(repeated_nodes, num_edges_per_node)

    return G
