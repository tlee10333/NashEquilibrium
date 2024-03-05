import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
import random
from typing import *


# Functions to calculate beta & alpha

def all_nash_pairs(n):
    """Calculates all the unique nash pairs in a list

    returns:
        A list containing tuples of unique nash pairs, in the format (node, node)"""

    pairs = []
    for node in n.prisoner_list:

        for i in n.nash_pair(node):
            if ((node, i) not in pairs) and ((i, node) not in pairs):
                pairs.append((node, i))
    return pairs


def alpha(n):
    """Given a network class, calculate percentage of nash pairs"""

    return 1 - (len(all_nash_pairs(n)) / n.G.size())


def beta(n):
    """Given a network class, calaculate percentage of cooperators in the entire graph"""
    cooperators = 0
    for node, prisoner in n.prisoner_list.items():
        if prisoner.get_strategy() == "C":
            cooperators += 1
    return cooperators / 1024


# Functions to create & run WS & NA Networks
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

            # Successfully make graphs with odd degrees/
        if k % 2 == 1 and u < n//2:
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

            # Remove itself & all it's neighbors to find al available choices for a new node to connect to.
            choices = nodes - {u} - set(G.neighbors(u))
            new_v = np.random.choice(list(choices))
            G.remove_edge(u, v)
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


# BA Graph Functions


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


# ER Graph

def all_pairs(nodes):
    """
    Generate all possible pairs of the elements of nodes

    Args:
      nodes: an iterable containing the objects to yield pairs of

    Yields:
      Every pair (tuple) of elements from nodes without repeats
    """
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i < j:
                yield u, v


def random_pairs(nodes, prob):
    """
    Generate each pair of elements of nodes with probability prob.

    Iterates through every pair of elements of nodes, and, for each pair, only
    yields it with probability prob

    Args:
      nodes: an iterable containing the objects to yield pairs of
      prob: a float from 0 to 1, the probability to yield each pair

    Yields:
      Pairs of the elements of nodes, where each pair has a probability prob of
        being yielded
    """
    for edge in all_pairs(nodes):
        if flip(prob):
            yield edge


def make_er_graph(num_nodes, prob_connected):
    """
    Create an Erdos-Renyi graph with num_nodes nodes and a p-value of
      prob_connected

    An Erdos-Renyi graph is generated by creating num_nodes nodes, and for each
    pair of nodes, connecting them with probability prob_connected

    Args:
      num_nodes: an int, the number of nodes to add to the graph
      prob_connected: a float from 0 to 1, the probability that any two given
        nodes are connected

    Returns:
      An Erdos-Renyi graph as a networkx Graph object
    """
    G = nx.Graph()
    nodes = range(num_nodes)
    G.add_nodes_from(nodes)
    G.add_edges_from(random_pairs(nodes, prob_connected))
    return G
