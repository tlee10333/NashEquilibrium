from networks import make_ws_graph

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns

class WS():
    '''

    A class that keep tracks of all individuals in a Watts-Strogatz Network for the Prisoner's Dilemma Game


    Attributes:
      ws: Graph that keeps track of the WS network
      prisoner_list: A dictionary which correlates each node in the ws to an individual Class
  
    
    '''
    
    def __init__(self, n,k,p) -> None:
      """
      Makes a Watts-Strogatz graph.

      Args:
        n: int, number of nodes
        k: int, degree of each node
        p: double, probability of rewiring an edge
      """
      self.ws = make_ws_graph(n,k,p)
      self.prisoner_list = {}


      # for node in list(self.ws.nodes()):
      #   self.prisoner_list[node] = individual
         

    def draw(self, labels=False):
      '''Draws the image of the WS network

      Args:
        labels: boolean, determines whether the graph will have labels of each node

      
      '''
      fig, ax = plt.subplots()
      pos = nx.spring_layout(self.ws)

      nx.draw_networkx(self.ws, node_color='C0', node_size=5, font_size=5, with_labels=False, pos=pos)
      plt.show()

    def round(self):
       
       

      

