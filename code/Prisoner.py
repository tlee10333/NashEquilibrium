import random

class Prisoner:
    def __init__(self, strat=None):
        possible_strats = ['C', 'D']
        self.strategy = strat
        
        if strat is None:
            self.strategy = random.choice(possible_strats)
        
        self.TRSP = {'T': 1, 'R': 2, 'P': 3, 'S': 4}
        self.strategy_history = [self.strategy]
        self.payoff_history = []

    def get_strategy(self):
        return self.strategy
    
    def set_strategy(self, x):
        self.strategy = x
    
    def get_payoff(self, j):
        if self.strategy == 'D' and j.get_strategy() == 'C':
            return self.TRSP['T']
        elif self.strategy == 'D' and j.get_strategy() == 'D':
            return self.TRSP['P']
        elif self.strategy == 'C' and j.get_strategy() == 'C':
            return self.TRSP['R']
        else:
            return self.TRSP['S']

    def update_payoff(self, j):
        if self.strategy == 'D' and j.get_strategy() == 'C':
            self.payoff_history.append(self.TRSP['T'])
            self.TRSP['T'] += 1
        elif self.strategy == 'D' and j.get_strategy() == 'D':
            self.payoff_history.append(self.TRSP['P'])
            self.TRSP['P'] += 1
        elif self.strategy == 'C' and j.get_strategy() == 'C':
            self.payoff_history.append(self.TRSP['R'])
            self.TRSP['R'] += 1
        else:
            self.payoff_history.append(self.TRSP['S'])
            self.TRSP['S'] += 1

    def get_previous_payoff(self):
        return self.payoff_history[-1]

    def add_to_strat_hist(self, x):
        self.strategy_history.append(x)

    def strat_history_append(self, x):
        self.strategy_history.append(x)
