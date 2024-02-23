import random

class Prisoner:
    def __init__(self, strat=None):
        """
        Implementation of the Prisoner object in the Prisoner's Dilemma Game

        Attributes:
            strat: a string (C or D) representing the Prisoner's initial strategy
        """
        possible_strats = ['C', 'D']
        self.strategy = strat
        
        if strat is None:
            self.strategy = random.choice(possible_strats)
        
        self.TRPS = {'T': 1, 'R': 2, 'P': 3, 'S': 4}
        self.strategy_history = [self.strategy]
        self.payoff = 0
        self.payoff_history = []

    ### STRATEGY ###
    def set_strategy(self, x):
        self.strategy = x

    def get_strategy(self):
        """
        Gets the Prisoner's current strategy

        Returns:
            A string (C or D) representing the Prisoner's current strategy
        """
        return self.strategy
    
    def add_to_strategy_history(self, x):
        self.strategy_history.append(x)
    
    ### PAYOFF ###
    def get_payoff(self):
        return self.payoff
    
    def get_previous_payoff(self):
        return self.payoff_history[-1]

    def update_payoff(self, j):
        if self.strategy == 'D' and j.get_strategy() == 'C':
            self.payoff += self.TRPS['T']
        elif self.strategy == 'D' and j.get_strategy() == 'D':
            self.payoff += self.TRPS['P']
        elif self.strategy == 'C' and j.get_strategy() == 'C':
            self.payoff += self.TRPS['R']
        else:
            self.payoff += self.TRPS['S']

    def reset_payoff(self):
        self.payoff = 0
    
    def add_to_payoff_history(self):
        self.payoff_history.append(self.payoff)

    ### OTHER ###

    def local_frequency(self):
        target = 'C'
        num_coop_rounds = [i for i in self.strategy_history if i==target]
        num_rounds_total = len(self.strategy_history)
        coop_rate = num_coop_rounds / num_rounds_total
        return coop_rate
