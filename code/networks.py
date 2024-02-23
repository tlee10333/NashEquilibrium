import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
import random
from typing import *


def adjacent_edges(nodes, k):
    """
    Yields edges between each node and `halfk` neighbors.

    Args:
      nodes: lists of ints representing the nodes on a graph
      halfk: int meaning the number of edges from each node
    """

    halfk = k//2



    n = len(nodes)
    for i, u in enumerate(nodes):
        for j in range(i+1, i+halfk+1):
            v = nodes[j % n]
            yield u, v

            #Successfully make graphs with odd degrees/
        if k % 2 ==1 and u < n//2:
          yield u, nodes[(n//2 + u)]


def make_ring_lattice(n, k):
    """
    Makes a ring lattice with `n` nodes and degree `k`.

    Note: this only works correctly if k is even.

    Args:
      n: int, number of nodes
      k: int, degree of each node

    Returns:
      networkx.Graph object which is a ring lattice with n nodes, each with
        degree k
    """
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)

    G.add_edges_from(adjacent_edges(nodes, k))


    return G


def rewire(G, p):
    """
    Rewires each edge with probability `p`.

    Args:
      G: networkx.Graph object, Graph to rewire
      p: float, probability that an edge gets rewired
    """

    nodes = set(G)
    for u, v in G.edges():
      if flip(p):

        #Remove itself & all it's neighbors to find al available choices for a new node to connect to.
        choices = nodes - {u} - set(G.neighbors(u))
        new_v = np.random.choice(list(choices))
        G.remove_edge(u,v)
        G.add_edge(u, new_v)


def flip(p):
    """
    Returns True with probability `p`.

    Args:
      p: float, probability that coin flips True
    """
    return np.random.random() < p

def make_ws_graph(n, k, p):
    """
    Makes a Watts-Strogatz graph.

    Args:
      n: int, number of nodes
      k: int, degree of each node
      p: double, probability of rewiring an edge

    Returns:
      networkx.Graph object of Watts-Strogatz graph with n nodes of degree k and
        probability p of edge being
    """
    ws = make_ring_lattice(n, k)
    rewire(ws, p)
    return ws




#BA Graph Functions


def make_ba_graph(num_nodes: int, num_edges_per_node: int,
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


def random_subset(repeated_nodes: List, num_to_select: int):
    """
    Select a random subset of nodes without repeats

    Args:
      repeated_nodes: list of nodes to randomly select from
      num_to_select: an int, the number of nodes to select

    Returns:
      A set of randomly selected elements of repeated_nodes, such that the
        length of the resulting set == num_to_select
    """
    targets = set()
    while len(targets) < num_to_select:
        node = random.choice(repeated_nodes)
        targets.add(node)
    return targets
