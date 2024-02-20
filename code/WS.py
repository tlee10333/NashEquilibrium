import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns

from utils import decorate, savefig

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

