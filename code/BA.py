import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
from typing import *
from networkx.algorithms.approximation import average_clustering
from networks import make_ba_graph


import random

class BA():
    
    def __init__(self, n,k ):
        """
        Generates a BA network
        
        n: number of nodes
        k: number of edges per nodes"""

        self.ba = make_ba_graph(n, k)
        
        self.prisoner_list = {}


      #50/50 of C & D when initally initalized

      #prisoner_list format {1: individual, 2: individual}
      # for node in list(self.ba.nodes()):
        #  if node <= 512:
      #     self.prisoner_list[node] = individual("C")
        #  else:
        #    self.prisoner_list[node] = individual("D")

    def draw(self, labels=False):
      '''Draws the image of the BA network
      Args:
        labels: boolean, determines whether the graph will have labels of each node
      '''
      fig, ax = plt.subplots()
      pos = nx.spring_layout(self.ba)

      nx.draw_networkx(self.ba, node_color='C0', node_size=5, font_size=5, with_labels=False, pos=pos)
      plt.show()

    def get_neighbors(self, node):
      return list(nx.all_neighbors(self.ba, node))


    def round(self):
      for node, prisoner in self.prisoner_list.items():
        neighbors = list(nx.all_neighbors(self.ba, node))
        prisoner_strategy = prisoner.get_strategy()

        #Play against each of it's neighbors
        for j in neighbors:
          #See what the payoff is
          neighbor_strategy = self.prisoner_list[j].get_strategy()
          prisoner.update_payoff(self.prisoner_list[j])
        prisoner.add_to_strat_history(prisoner_strategy)
          
          


    def update(self, rule=0):
      for node in self.prisoner_list:
        #Nowak & May Updating Rule
        if rule ==0:
          self.nowak_may(node)
        if rule == 1:
          self.santos_pacheco(node)
        node.reset_payoff()

      

    def nowak_may(self, node):
      prisoner = self.prisoner_list[node]
      neighbors = list(nx.all_neighbors(self.ba, node))
      highest_payoff = prisoner.get_previous_payoff()
      strategy = prisoner.get_strategy()
      for j in neighbors:
        neighbor = self.prisoner_list[j]
        if neighbor.get_previous_payoff() > highest_payoff:
          highest_payoff = neighbor.get_previous_payoff()
          strategy = neighbor.get_previous_strategy()
      
      prisoner.update_strategy(strategy)
    
    def santos_pacheco(self, prisoner):
      neighbors = list(nx.all_neighbors(self.ba, prisoner))
      prisoner_payoff = prisoner.get_previous_payoff()
      neighbor = random.choice(neighbors)

      if neighbor.get_previous_payoff() > prisoner_payoff:
        switch_prob = (neighbor.get_previous_payoff() - prisoner_payoff)/(neighbor.get_previous_payoff() + prisoner_payoff)

        #Switch to new payoff
        if random.random() < switch_prob:
          prisoner.set_strategy(neighbor.get_previous_strategy())



        



      

  



    

      
       
  





        
        