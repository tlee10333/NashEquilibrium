from networks import make_ws_graph, make_ba_graph, flip
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
      prisoner_list: A dictionary which correlates each node in the ws to an individual Clas
    '''

    def __init__(self, n, k, prob=0.1, graph_type="ws", t=4, r=3, p=2, s=1) -> None:
        """
        Makes a Watts-Strogatz graph.

        Args:
          n: int, number of nodes
          k: int, degree of each node
          prob: double, probability of rewiring an edge
        """

        self.n = n
        if graph_type == "ws":

            self.G = make_ws_graph(n, k, prob)
        elif graph_type == "ba":
            self.G = make_ba_graph(n, k)

        self.prisoner_list = {}

        # 50/50 of C & D when initally initalized
        # prisoner_list format {1: individual, 2: individual}
        for node in list(self.G.nodes()):

            prob = flip(0.5)
            if prob:
                # if node < n/2:
                self.prisoner_list[node] = Prisoner("C", t=t, r=r, p=p, s=s)
            else:
                self.prisoner_list[node] = Prisoner("D", t=t, r=r, p=p, s=s)

    def get_neighbors(self, node):
        """Returns a list of neighbors of a specified individual

        args:
          node: int that represents the number of the individual we're interested in

        returns:
          A list of int which represent the number IDs of the neighbors """
        return list(nx.all_neighbors(self.G, node))

    def draw(self, labels=False):
        '''Draws the image of the WS network. Color coded so Red represents defectors and blue represents cooperators

        Args:
          labels: boolean, determines whether the graph will have labels of each node
        '''

        fig, ax = plt.subplots()

        pos = nx.spring_layout(self.G)

        def assign_color(node):
            '''A private function that basically determines the color of the prisoner'''
            return 'red' if self.prisoner_list[node].get_strategy() == "D" else 'blue'

        node_colors = [assign_color(node) for node in self.G.nodes]
        nx.draw_networkx(self.G, node_color=node_colors,
                         node_size=5, font_size=5, with_labels=False, pos=pos)

        plt.show()

    def subplot_draw(self):
        '''Draws the image of the WS network. Color coded so Red represents defectors and blue represents cooperators

        Args:
          labels: boolean, determines whether the graph will have labels of each node
        '''

        pos = nx.spring_layout(self.G)

        def assign_color(node):
            '''A private function that basically determines the color of the prisoner'''
            return 'red' if self.prisoner_list[node].get_strategy() == "D" else 'blue'

        node_colors = [assign_color(node) for node in self.G.nodes]
        nx.draw_networkx(self.G, node_color=node_colors,
                         node_size=5, font_size=5, with_labels=False, pos=pos)

    def round(self):
        '''Runs one round of PDG

        For each prisoner, they play PDG will all their neighbors using their current strategy for the entire round. After reach game with it's neighbor, their payoff value will be adjusted according to which payoff they got. At the end, their total payoff value determines how well they did that round against their opponents'''

        for node, prisoner in self.prisoner_list.items():
            neighbors = list(nx.all_neighbors(self.G, node))
            prisoner_strategy = prisoner.get_strategy()

            # Play against each of it's neighbors
            for j in neighbors:
                # See what the payoff is
                neighbor = self.prisoner_list[j]
                prisoner.update_payoff(self.prisoner_list[j])

                prisoner_delta_n = (prisoner.TRPS["S"] - prisoner.TRPS["P"] + (
                    prisoner.TRPS["R"] - prisoner.TRPS["T"] + prisoner.TRPS["P"] - prisoner.TRPS["S"]) * prisoner.local_frequency())

                neighbor_delta_n = (neighbor.TRPS["S"] - neighbor.TRPS["P"] + (
                    neighbor.TRPS["R"] - neighbor.TRPS["T"] + neighbor.TRPS["P"] - neighbor.TRPS["S"]) * neighbor.local_frequency())

                if (neighbor_delta_n > 0 and prisoner_delta_n > 0) or (neighbor_delta_n < 0 and prisoner_delta_n < 0):
                    prisoner.add_nash_pair(j)  # Add neighbor's node

            prisoner.add_to_strategy_history(prisoner_strategy)
            prisoner.add_to_payoff_history()

    def update(self, rule=0):
        """Prepare for next round & choose strategy using either nowak-may or santos-pacheco updating rule

        args:
          rule: determines the type of updating rule. 0 means Nowak-may and 1 means santos-pacheco"""

        for node in self.prisoner_list:
            self.prisoner_list[node].reset_payoff()
            self.prisoner_list[node].clear_nash_pair()

            # Nowak & May Updating Rule
            if rule == 0:
                self.nowak_may(node)
            if rule == 1:
                self.santos_pacheco(node)

    def nowak_may(self, node):
        """Uses the Nowak & May Updating Rule
        1. Look at all the neighbors of a prisoner
        2. Choose the neighbor who had the highest payoff in the last round
        3. Prisoner adopts the neighbor's strategy in the last round for this round
        args:
          node: An integer that represents the node we're working with in the gram
        """
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
        """Uses the Santos-Pacheco updating rule
        1. Out of their neighbors, randomly chooses one neighbor
        2. If their neighbor's payoff last round was higher than prisoner's payoff, they have a (neighbor_payoff - prisoner_payoff)/(neighbor_payoff - prisoner_payoff) percentage of adopting the neighbor's strategy. 

        args:
          node: integer that represents the node the prisoner is
        """
        prisoner = self.prisoner_list[node]

        neighbors = list(nx.all_neighbors(self.G, node))
        prisoner_payoff = prisoner.get_previous_payoff()
        neighbor = self.prisoner_list[random.choice(neighbors)]

        if neighbor.get_previous_payoff() > prisoner_payoff:
            switch_prob = (neighbor.get_previous_payoff() - prisoner_payoff) / \
                (neighbor.get_previous_payoff() + prisoner_payoff)

            # Switch to new payoff
            if random.random() < switch_prob:
                prisoner.set_strategy(neighbor.get_previous_strategy())

    def nash_pair(self, node):
        return self.prisoner_list[node].nash_paired