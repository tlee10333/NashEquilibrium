import random

class Prisoner:
    def __init__(self):
        strategies = ['C', 'D']
        self.strategy = random.choice(strategies)
        self.TRSP = {'T': 1, 'R': 2, 'P': 3, 'S': 4}

    def get_strategy(self):
        return self.strategy
    
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
            self.TRSP['T'] += 1
        elif self.strategy == 'D' and j.get_strategy() == 'D':
            self.TRSP['P'] += 1
        elif self.strategy == 'C' and j.get_strategy() == 'C':
            self.TRSP['R'] += 1
        else:
            self.TRSP['S'] += 1
          
