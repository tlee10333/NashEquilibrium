import random

class Prisoner:
    def __init__(self, strat=None):
        """
        Implementation of the Prisoner object in the Prisoner's Dilemma Game.

        Args:
            - strat (str): The prisoner's initial strategy. 'C' represents cooperation, 'D' represents defection.

        Attributes:
            - TRPS (dict):  The payoffs for different combinations of strategies.
                            Keys represent the opponent's strategy, and values represent the corresponding payoff.
                            'T': Temptation, 'R': Reward, 'P': Punishment, 'S': Sucker.
            - strategy (str): The prisoner's strategy. 'C' represents cooperation, 'D' represents defection.
            - strategy_history (list of str): The prisoner's past strategies in the previous rounds.
            - payoff (int): The value of the outcome of the current round.
            - payoff_history (list of int): The prisoner's past payoffs in the previous rounds.
        """

        self.TRPS = {'T': 4, 'R': 3, 'P': 2, 'S': 1}
        possible_strats = ['C', 'D']
        self.strategy = strat
        
        if strat is None:
            self.strategy = random.choice(possible_strats)

        self.strategy_history = [self.strategy]
        self.payoff = 0
        self.payoff_history = []

    ### STRATEGY ###
    def set_strategy(self, strat):
        """
        Sets the strategy of the prisoner.

        Args:
            strat (str): The new strategy to be set. 'C' represents cooperation,
                         'D' represents defection.
        """
        self.strategy = strat

    def get_strategy(self):
        """
        Gets the strategy of the prisoner.
        
        Returns:
            strategy (str): The prisoner's strategy. 'C' represents cooperation, 'D' represents defection.
        """
        return self.strategy
    
    def get_previous_strategy(self):
        """
        Gets the previous strategy of the prisoner.
        
        Returns:
            strategy (str): The prisoner's strategy. 'C' represents cooperation, 'D' represents defection.
        """
        return self.strategy_history[-1]
    def add_to_strategy_history(self, strat):
        """
        Adds a value to the strategy history list of the prisoner.
        
        Args:
            strat (str): The value to be added to the strategy history list.
        """
        self.strategy_history.append(strat)
    
    ### PAYOFF ###
    def get_payoff(self):
        """
        Gets the payoff of the current round.
        
        Returns:
            payoff (int): The value of the outcome of the current round.
        """
        return self.payoff
    
    def get_previous_payoff(self):
        """
        Gets the payoff of the previous round by retreiving the last element of the payoff history list.
        
        Returns:
            The payoff of the previous round.
        """
        return self.payoff_history[-1]

    def update_payoff(self, j):
        """
        Gets the payoff of the previous round by retreiving the last element of the payoff history list.
        Returns:

        Args:
            j: The 

        Returns:
            The payoff of the previous round.
        """
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
