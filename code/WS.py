from networks import make_ws_graph, make_ba_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
import random
from Prisoner import *


class Network():
    '''

    A class that keep tracks of all individuals in a Watts-Strogatz Network for the Prisoner's Dilemma Game


    Attributes:
      ws: Graph that keeps track of the WS network
      prisoner_list: A dictionary which correlates each node in the ws to an individual Class
  
    
    '''
    
    def __init__(self, n,k,p=0.1, graph_type="ws") -> None:
      """
      Makes a Watts-Strogatz graph.

      Args:
        n: int, number of nodes
        k: int, degree of each node
        p: double, probability of rewiring an edge
      """

      if graph_type == "ws":

        self.G = make_ws_graph(n,k,p)
      elif graph_type == "ba":
        self.G = make_ba_graph(n, k)

      self.prisoner_list = {}


      #50/50 of C & D when initally initalized
      #prisoner_list format {1: individual, 2: individual}
      for node in list(self.G.nodes()):
        if node <= 512:
          self.prisoner_list[node] = Prisoner("C")
        else:
          self.prisoner_list[node] = Prisoner("D")
            
    

    def get_neighbors(self, node):
      return list(nx.all_neighbors(self.G, node))



    def draw(self, labels=False):
      '''Draws the image of the WS network

      Args:
        labels: boolean, determines whether the graph will have labels of each node

      
      '''
      fig, ax = plt.subplots()
      pos = nx.spring_layout(self.G)

      def assign_color(node):
        return 'red' if self.prisoner_list[node].get_strategy() == "D" else 'blue'

      node_colors = [assign_color(node) for node in self.G.nodes]




      nx.draw_networkx(self.G, node_color=node_colors, node_size=5, font_size=5, with_labels=False, pos=pos)
      plt.show()

    def round(self):

      for node, prisoner in self.prisoner_list.items():
        neighbors = list(nx.all_neighbors(self.G, node))
        prisoner_strategy = prisoner.get_strategy()

        #Play against each of it's neighbors
        for j in neighbors:
          #See what the payoff is
          neighbor_strategy = self.prisoner_list[j].get_strategy()
          prisoner.update_payoff(self.prisoner_list[j])
        prisoner.add_to_strategy_history(prisoner_strategy)
        prisoner.add_to_payoff_history()
          
          

    def update(self, rule=0):
      """Prepare for next round & choose strategy"""
      
      for node in self.prisoner_list:
        self.prisoner_list[node].reset_payoff()

        #Nowak & May Updating Rule
        if rule ==0:
          self.nowak_may(node)
        if rule == 1:
          self.santos_pacheco(node)

      

    def nowak_may(self, node):
      prisoner = self.prisoner_list[node]
      neighbors = list(nx.all_neighbors(self.G, node))
      highest_payoff = prisoner.get_previous_payoff()
      strategy = prisoner.get_strategy()
      for j in neighbors:
        neighbor = self.prisoner_list[j]
        if neighbor.get_previous_payoff() > highest_payoff:
          highest_payoff = neighbor.get_previous_payoff()
          strategy = neighbor.get_previous_strategy()
      
      prisoner.set_strategy(strategy)
    
    def santos_pacheco(self, node):
      prisoner = self.prisoner_list[node]

      neighbors = list(nx.all_neighbors(self.G, node))
      prisoner_payoff = prisoner.get_previous_payoff()
      neighbor = self.prisoner_list[random.choice(neighbors)]

      if neighbor.get_previous_payoff() > prisoner_payoff:
        switch_prob = (neighbor.get_previous_payoff() - prisoner_payoff)/(neighbor.get_previous_payoff() + prisoner_payoff)

        #Switch to new payoff
        if random.random() < switch_prob:
          prisoner.set_strategy(neighbor.get_previous_strategy())
