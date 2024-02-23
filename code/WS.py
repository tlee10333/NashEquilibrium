from networks import make_ws_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
import random

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


      #50/50 of C & D when initally initalized

      #prisoner_list format {1: individual, 2: individual}
      # for node in list(self.ws.nodes()):
        #  if node <= 512:
      #     self.prisoner_list[node] = individual("C")
        #  else:
        #    self.prisoner_list[node] = individual("D")
            
    

    def get_neighbors(self, node):
      return list(nx.all_neighbors(self.ws, node))



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
      for node, prisoner in self.prisoner_list.items():
        neighbors = list(nx.all_neighbors(self.ws, node))
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
      neighbors = list(nx.all_neighbors(self.ws, node))
      highest_payoff = prisoner.get_previous_payoff()
      strategy = prisoner.get_strategy()
      for j in neighbors:
        neighbor = self.prisoner_list[j]
        if neighbor.get_previous_payoff() > highest_payoff:
          highest_payoff = neighbor.get_previous_payoff()
          strategy = neighbor.get_previous_strategy()
      
      prisoner.update_strategy(strategy)
    
    def santos_pacheco(self, prisoner):
      neighbors = list(nx.all_neighbors(self.ws, prisoner))
      prisoner_payoff = prisoner.get_previous_payoff()
      neighbor = random.choice(neighbors)

      if neighbor.get_previous_payoff() > prisoner_payoff:
        switch_prob = (neighbor.get_previous_payoff() - prisoner_payoff)/(neighbor.get_previous_payoff() + prisoner_payoff)

        #Switch to new payoff
        if random.random() < switch_prob:
          prisoner.set_strategy(neighbor.get_previous_strategy())



        



      

  



    

      
       
  