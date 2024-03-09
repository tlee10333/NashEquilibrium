# Investigating Nash Equilibrium in Social Networks through the Prisoner’s Dilemma Game: A Replication Study and Analysis of Simulation Results

Trinity Lee and Daniel Quinteros

### Abstract												
Nash equilibrium is a concept in evolutionary game theory where the game reaches an optimal outcome and individuals in the game no longer have an incentive to change their strategy. To investigate the Nash equilibrium phenomena in social networks, we used the Prisoner’s Dilemma Game (PDG) to observe how strategy equilibrium emerges in different types of social networks. 

Overall,, we investigated the local Nash Equilibrium phenomenon in social networks by observing a total of four different types of networks: Watt-Strogatz small-world networks (WS), Barabasi-Albert scale-free networks (BA), Erdo-Renyi Random networks (ER), and Newman-Watts (NW) small-world networks.

By tracking the fraction of Nash pairs (a pair of individuals in Nash Equilibrium)  and the proportion of cooperators within the entire population, we can find if and when the networks reach Nash equilibrium.

### Methodology

In the PDG, there are two strategies an agent could choose: Cooperator or Defector. For the PDG, there are four defined parameters that influence agent-based behavior: T (temptation to defect) for defecting a cooperator, R (reward for mutual cooperation) for cooperating with a cooperator, P (punishment for mutual defection) for defecting a defector, and S (sucker’s payoff) for cooperating with a defector. The parameters follow these rules T > R > P ≥ S and 2R > T + S so that defecting has the highest possible payoff from the prospective of the two person group. 

For each round, the agents can then adjust their strategies simultaneously according to a certain updating rule of strategy. We utilized two different Darwinian approaches, Nowak & May and Santos & Pachecos. 

###### Nowak and May 
Nowak and May is an updating rule where at the beginning of each round, each player/prisoner will choose the strategy they will use for the current round by looking through all their neighbors and using the last round’s strategy of the neighbor who had the highest payoff. If the player’s payoff is higher than any of its neighbors, it will keep its strategy from the last round. 

##### Santos and Pachecos
Santos and Pacheco is a local random evolution updating rule. At the beginning of each round, each player/prisoner will randomly choose one of its neighbors. It will then compare the neighbor’s payoff from the last round, and if it is higher than the player’s payoff in the last round, the player/prisoner will have a probability directly proportional to the difference in payoff to adopt the neighbor’s strategy for the current round. 

#### Network Simulation & Parameters
In this study, we observe the system’s Nash equilibrium in four different networks: WS, BA, ER, and NW. Each network has exactly 1024 nodes, with 50% starting as defectors and 50% starting off as cooperators. Each node has a degree of 6. For graphs that could be re-wired (i,e Watts-Strogatz), we set the probability to 10%. For the Newman-Watts graph, the degree of each node is varied because while each node starts with a degree of 6, it has a 10% chance of adding a new edge to the node.

During a simulation, we observe the percentage of cooperators and Nash pairs within a system throughout 500 timesteps. Unlike the original paper (see in the annotated bibliography), we could not achieve 11,000 timesteps due to time complexity restraints nor run each simulation 10 times and take its average. This is because each simulation could vary in time length. For example, running one simulation of WS of 500 timesteps, it required around 10 minutes. However, for ER, BA, and NW graphs, it took on average 60 minutes for 500 timesteps. 

Because each node has multiple neighbors, in each round, each node will play a round with each of their neighbors. Hence, per round, every node will have an average of playing the game 6 times with their neighbors. For each neighbor, they must use the same strategy for the entire round. Every game has the result of adding or subtracting to the prisoner’s payoff. At the end of each round, we calculate the total payoff of each individual and use that as a metric for how well each prisoner did with their strategy. This also means that a single node can be in Nash pairs with multiple nodes.

#### Nash Pairs
In an attempt to measure if a pair of prisoners are in Nash equilibrium, we calculate whether both nodes chose a strategy that maximized their payoff regardless of their partner’s strategy. If they both have, then we can declare that they are a Nash pair. 

Throughout the simulation, the number of Nash pairs and the number of cooperators & defectors were kept track of to understand what was the best personal strategy for survival given different parameter values, networks, and update laws. α is the percentage of total unique Nash pairs in the network. 

We used Local Nash equilibrium to judge whether a gaming structured population reached the evolutionary stable state and predicted whether cooperation could exist in a system long before the system reached its evolutionary stable state. The experiment’s variables include the type of network being used (WS or BA), the values assigned to the four parameters that influence agent-based behavior, and the updating rule utilized.

### Results
We ran a parameter sweep on WS and BA networks for T (temptation to defect) from values of 1.1 to 2.0. For the other parameters, P=0, S=0, and R=1. For each WS and BA network, we also ran a simulation using the Nowak and May updating rule and a simulation with the Santos and Pacheco updating rule. Below are the results for α (percentage of unique Nash pairs in the system) and β (percentage of cooperators) over 500 timesteps. 

![alpha_parameter_sweep](https://github.com/tlee10333/NashEquilibrium/assets/47285707/ca83a2aa-c512-4c7a-a0fa-7bd3ef16a0b2)

**Figure 1: The evolution of α**, representing the fraction of Nash pairs in the connected individuals, for the PDG in social networks. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![beta_parameter_sweep](https://github.com/tlee10333/NashEquilibrium/assets/47285707/c1683682-0b9d-489f-ab0b-39bf55819bd9)

**Figure 2: The evolution of β**, representing the proportion of cooperators within the entire population of players at a particular round (n) of the game. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![Original Graphs v2](https://github.com/tlee10333/NashEquilibrium/assets/47285707/37f03b56-7924-4f95-b43b-15e340d3ccde)

**Figure 3: Parameter sweep of a Nowak & May WS Graph** from T = 1.1 to T = 1.6. These are the original graphs corresponding to plot (A) in both Figure 1 and Figure 2. For the sake of viewability, only the first six graphs are shown. The other graphs, from T = 1.7 to T = 2.0 are visibly indistinguishable from T = 1.6, with the large majority of nodes being defectors.

### Interpretation

In Figure 1, the decay of α is prevalent for the temptation to defect T < 1.5 in (A), T < 1.4 in (B), T < 1.9 in (C) and T < 2.0 in (D). Conversely, α stabilizes at a high value above the mentioned threshold values. In these instances, our simulation findings for β in Figure 2 indicate that cooperators can persist in the corresponding states.

None of our models managed to achieve a stabilization point at α = 1. Instead, they stabilized at a minimum level with slight fluctuations. Seeing as cooperators can survive in the system, it implies that cooperative behavior is sustainable and beneficial for individuals within the system. Consequently, one would expect to observe an increasing presence of cooperators within the Nash pairs over time, indicating their successful engagement and influence on other individuals. Having said that, this would mean that the introduction of cooperators possibly disrupts existing equilibria or alters the dynamics of interactions. This disruption or alteration is potentially what leads to a decrease in the fraction of Nash pairs (α) over time in some of the system models.

Eventually, the system reaches an evolutionary stable state, characterized by stability and equilibrium in the strategies adopted by individuals. At this point, α stabilizes at its minimum value, possibly with minor fluctuations. This indicates that the system has settled into a relatively stable configuration where cooperative behavior is sustainable.

In contrast, if cooperators cannot survive in the system, α grows over time and approaches a value of 1, as observed in plot (A) of Figure 1 when T ≥ 1.5. This suggests a dominance of non-cooperative strategies, possibly leading to instability or unfavorable outcomes for individuals within the system. Once again, this is seen in Figure 3, where there is a stark increase in defectors when T ≥ 1.5.

### Replication Accuracy

![study_results_cropped](https://github.com/tlee10333/NashEquilibrium/assets/47285707/ec38ea07-7183-41db-8cee-18859c9a9ef5)

**Figure 4: The results from the “Local Nash Equilibrium in Social Networks” paper [1]**, showing the evolution of α and β for the PDG in social networks, ranging from T = 1.1 to T = 2.0, on the system. (a, e) and (c\, g) show the simulation results obtained by the updating rule proposed by Nowak and May on the WS small-world networks and BA scale-free networks, respectively. (b, f) and (d, h) show the simulation results obtained by the updating rule proposed by Santos and Pacheco on both networks, respectively.

The graphs in Figure 4 illustrate the evolution of α and β, representing our sought-after replication results. Upon examining the α plots, there is a clear resemblance between our findings and those of the referenced study. A notable disparity we found was that our graphs closely mirrored the paper’s exhibit a shift so that the early trends are not visible. Looking at the β plots, although they are visualized differently, they bear a resemblance to the study's outcomes.

In general, we see that our simulation does in general align with behavior that the study noted. For example, whenever alpha reaches or is close to one, the paper notes that no cooperators can survive because all the defectors will be in Nash pairs. This behavior closely aligns with our parameter sweep results. As the value of T gets larger, certain graphs—like the Nowak & May WS network—will reach Nash equilibrium (alpha approaches 1) while the number of cooperators decreases to 0. 

![four_graphs_comparison(1)](https://github.com/tlee10333/NashEquilibrium/assets/47285707/79a8a17e-08fa-4190-a379-ecf9c47cbaf0)

**Figure 5: Comparison of the evolution of α and β** for the PDG in social networks when T = 1.2 between our results (left) and the results of the “Local Nash Equilibrium in Social Networks” paper (right) [1]. 

Upon conducting a more detailed comparison with our simulations in Figure 5, it becomes evident that our results generally align with those of the paper, barring the evolution of α in the Nowak and May BA simulation. These graphs, used by the referenced paper, served to illustrate how, sometimes, models can incorrectly characterize systems as being in Nash equilibrium because they observe two long temporary stable states in the black rectangles. Notably, our results lack these temporary stable states; instead, they tend to approach 1 or decay to a local minimum, a behavior we deemed a non-issue.

For our extension, we conducted another PDG simulation, but with two new graphical network types: Erdos Renyi (ER) and Newmann-Watts (NW). We were curious to see how alpha and beta would behave on two different types of network graphs and whether we would find any surprising results. For each new network, we did a parameter sweep exactly the way we did with the BA and WS graphs. 

#### Erdos-Renyi
The Erdos-Renyi random graph is a type of network where given a random set of nodes, we then randomly rewire edges based on a set probability and degree. 

### Extension![extension_ER](https://github.com/tlee10333/NashEquilibrium/assets/47285707/9c19d78c-90b9-430c-9247-704fe2acf6c7)

**Figure 6: The evolution of α and β in a Nowak May ER graph model and a Santos-Pacheco ER graph model**. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![ER_graphs](https://github.com/tlee10333/NashEquilibrium/assets/47285707/b63793a6-a06b-456a-985d-f01b9abf4cd4)

**Figure 7: Parameter sweep of a Nowak & May ER graph** ranging from T = 1.1 to T = 1.3. These graphs are the original representations corresponding to plots (A) and (C) in Figure 6. To enhance visibility, only the first three graphs are displayed. Subsequent graphs, from T = 1.4 to T = 2.0, exhibit no discernible differences compared to T = 1.3, with the vast majority of nodes identified as defectors. Similarly, the trends observed in the aforementioned figure and described therein are also evident in the Santos and Pacheco ER graphs.

#### Newman-Watts
The Newman-watts graph is a variation of the Watts-Strogatz network graph. Just like a WS model, we start with a ring lattice. However, instead of rewiring existing edges, we add new edges when rewiring. Hence, the degree of each node varies based on probability p. 

![extension_nw](https://github.com/tlee10333/NashEquilibrium/assets/47285707/00e29d37-cef2-4cb3-ab3e-86c9564dca5d)

**Figure 8: The evolution of α and β in a Nowak May NW graph model and a Santos-Pacheco NW graph model**. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![NW_graphs](https://github.com/tlee10333/NashEquilibrium/assets/47285707/ad62e75f-300f-4851-ae90-5f22fd2e94ee)

**Figure 9: Parameter sweep of a Nowak & May NW graph** ranging from T = 1.1 to T = 1.8. These graphs are the original representations corresponding to plots (A) and (C) in Figure 8. To enhance visibility, only the first eight graphs are displayed. Subsequent graphs, from T = 1.9 to T = 2.0, exhibit no discernible differences compared to T = 1.8, with the vast majority of nodes identified as defectors.

#### Extension Interpretations
The ER and NW graphs had very surprising results that were distinctly different from the BA and WS graphs. For example, the Nowak & May ER graph almost instantly reached Nash equilibrium of all defectors once T >1.1, as seen in Figures 6 and 7. One explanation for this is that because ER graphs are not fully connected, it could mean that extremely isolated clusters end up benefiting defectors more than cooperators, leading to an almost immediate takeover of defectors and thus reaching Nash Equilibrium early on. In that same sense, when we use the Santos-Pacheco rule, because of its random nature, it could lead to higher survival of cooperators since clusters with large numbers of cooperators could survive invasions of defectors. 

As for the NW results (seen in Figure 8), the behavior of alpha over time generally looks similar to the WS graph, which makes sense as both are variations of the same small-world network graphs. There are slight differences though, like how the Nowak-May WS plateaus for values of 1.3< T <1.5 while the Nowak-May NW network graphs end up approaching 0 or 1 for alpha values. Another distinction is that while the Santos-Pacheco NW graph tends to plateau for alpha in for T=1.3 and 1.4, the Santos-Pacheco WS graph alpha value continues to decrease for T=1.3 and 1.4. 

Another distinct difference between NW and WS networks is the distribution of betas.  The NW beta distribution is distinctly different from the WS beta distribution. Furthermore, for the NW graph, at T=1.6, we see that it is strongly dominated by cooperators (seen in Figure 9), which is unusual with a temptation value that high. In general, for lower values of T in WS graphs, clusters of cooperators can survive amid defectors or maintain an equal ratio between defector and cooperator in a network. However, the inverse is true for NW where clusters of defectors can survive amid cooperators, but it is almost impossible for clusters of cooperators to survive amid defectors. There are no good explanations for why this occurs, except that due to the higher number of edges, it may lead to reaching an evolutionary stable state faster for NW graphs while WS takes longer to reach the stable state. 

### Causes for Concern

One of the main causes for concern is the failure to perfectly replicate their results. The first caveat of our research is that while they ran their simulations for around 11,000 steps each, with each parameter sweep consisting of multiple repeated simulations just in case, we only did up to 500 timesteps and only did a simulation per parameter sweep. This means that we cannot fully confirm if our networks have reached a true evolutionary stable state as 500 timesteps are barely enough compared to 11,000 timesteps. The reason why we were not able to do 11,000 and take the average of multiple simulations was due to the time complexity of the program. While running 500 steps for 10 different simulations for WS graphs took around 7-9 minutes total, simply running 10 simulations for 500 steps in BA graphs, took on average 45-55 minutes. Given that it took that much to run the BA graphs, it did not seem feasible for us to go for 11,000 steps total.

We chose 500 timesteps because when we looked at the research paper, it seemed that alpha had stabilized around the 500-1000 timestep mark. Hence, while we chose 500 as a reasonable compromise between runtime and accuracy to the original research conditions, it is important to acknowledge that the findings are not completely identical to the research paper.

Furthermore, there were definitely some graphs that did not match the picture perfectly to the results of the Nash Equilibrium paper. This is also a cause of concern since most of the graphs seem to align with what we expected, but there are some unexplainable behaviors that we noticed.  

### Annotated Bibliography
[1] [Local Nash Equilibrium in Social Networks](https://www.nature.com/articles/srep06224.pdf#:~:text=The%20local%20Nash%20equilibrium%20provides%20a%20way%20to,evolutionary%20stable%20state%20for%20the%20Prisoner%E2%80%99s%20dilemma%20game) **Yichao Zhang, M. A. Aziz-Alaoui, Cyrille Bertelle & Jihong Guan**
This paper investigated two different imperfect information games, The Prisoner’s Dilemma, and the Snow Drift/Hawk-Dove/Chicken, and saw how an evolutionary stable state emerged (using local Nash equilibrium to measure) when these two games were placed in a small world (WS) and scale-free (BA) networks.

