#Constants

#4 Parameters
t_param =0 #(temptation to defect) for defecting a cooperator
r_param =0 #(reward for mutual cooperation) for cooperating with a cooperator
t_param =0 #(punishment for mutual defection) for defecting a defector
s_param =0 #(sucker’s payoff) for cooperating with a defector.

# For individual i, it plays with it's k neighbors. This is kept track through an adjacency matrix of the network. it'

# Each round i can either be 1 (cooperator) or 0 (defector)

#Rules that guide the different parameter payoffs
#T > R >  P >= S and 
# 2R >  T + S --makes mutual cooperation the best outcome 



#W(n) = local frequency  -> literally means % of cooperating out of everyone

adj_matrix = [[0,1,1],[1,0,0],[1,0,0]]


for i, j in enumerate(adj_matrix):
    sum = i * 
    


# beta = frequency of cooperators in a newtowrk 
#alpha = % of nash pairs of the entire network
#gamma  = number of defectors in a nash pair

# Payoff: delta(N) = S - P + (R -T +P -S) * W(n)

#Max payoff: if delta(n) == 0, rand
# if delta(n) > 0, then they must be cooperator
# if delta(n) < 0, then they must be a defector

#
X_i = 1
A = [0,1]
neighbors = 1


i
import networks

ws = networks.make_ws_graph(1024, 6, 0.1)
ba = networks.BA(1024, 6)

