# Investigating Nash Equilibrium in Social Networks through the Prisoner’s Dilemma Game: A Replication Study and Analysis of Simulation Results

Trinity Lee and Daniel Quinteros

### Abstract
Nash equilibirum is the concept where the game reaches an optimal outcome and individuals in the game no longer have an incentive to change their strategy. Additionally, a nash pair is a pair of individuals who are are nash equilibrium.

We investigated the local Nash Equilibrium phenomenon in social networks by simulating the Prisoner’s Dilemma Game (PDG). These simulations integrated two types of networks: Watts and Strogatz small-world networks (WS) and Barabasi and Albert scale-free networks (BA).

By tracking the fraction of nash pairs and the proportion of cooperators within the entire population, we can find if and when the networks reach nash equilibrium.

### Methodology

In the PDG, there are two strategies an agent could choose: Cooperator or Defector. For the PDG, there are four defined parameters that influence agent-based behavior: T (temptation to defect) for defecting a cooperator, R (reward for mutual cooperation) for cooperating with a cooperator, P (punishment for mutual defection) for defecting a defector, and S (sucker’s payoff) for cooperating with a defector. The parameters follow these rules T > R > P ≥ S and 2R > T + S so that mututal cooperation is the best outcome from the prospective of the two person group.

Furthermore, the agents can then adjust their strategies simultaneously according to a certain updating rule of strategy. They utilized two different approaches, Nowak & May and Santos & Pachecos. [Explain updating rules briefly]

Throughout the simulation, the number of Nash pairs and number of cooperators & defectors were kept track of to understand what was the best personal strategy for survival given different parameter values, networks, and update laws.

We used Local Nash equilibrium to judge whether a gaming structured population reached the evolutionary stable state and predicted whether cooperation could exist in a system long before the system reached its evolutionary stable state. The experiment’s variables include the type of network being used (WS or BA), the values assigned to the four parameters that influence agent-based behavior, and the updating rule utilized.

### Results

![alpha_parameter_sweep](https://github.com/tlee10333/NashEquilibrium/assets/47285707/ca83a2aa-c512-4c7a-a0fa-7bd3ef16a0b2)

**Figure 1: The evolution of α**, representing the fraction of Nash pairs in the connected individuals, for the PDG in social networks. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![beta_parameter_sweep](https://github.com/tlee10333/NashEquilibrium/assets/47285707/c1683682-0b9d-489f-ab0b-39bf55819bd9)

**Figure 2: The evolution of β**, representing the proportion of cooperators within the entire population of players at a particular round (n) of the game. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![Original Graphs v2](https://github.com/tlee10333/NashEquilibrium/assets/47285707/37f03b56-7924-4f95-b43b-15e340d3ccde)

**Figure 3: Parameter sweep of a Nowak & May WS Graph** from T = 1.1 to T = 1.6. These are the original graphs corresonding to plot (A) in both Figure 1 and Figure 2. For the sake of viewability, only the first six graphs are shown. The other graphs, from T = 1.7 to T = 2.0 are visibily indistinguisable from T = 1.6, with the large majority of nodes being defectors.

### Interpretation

In Figure 1, the decay of α is prevalent for the temptation to defect T < 1.5 in (A), T < 1.4 in (B), T < 1.9 in (C) and T < 2.0 in (D). Conversely, α stabilizes at a high value above the mentioned threshold values. In these instances, our simulation findings for β in Figure 2 indicate that cooperators can persist in the corresponding states.

None of our models managed to achieve a stabilization point at α = 1. Instead, they stabilized at a minimum level with slight fluctuations. Seeing as cooperators can survive in the system, it implies that cooperative behavior is sustainable and beneficial for individuals within the system. Consequently, one would expect to observe an increasing presence of cooperators within the Nash pairs over time, indicating their successful engagement and influence on other individuals. Having said that, this would mean that the introduction of cooperators possibly disrupts existing equilibria or alters the dynamics of interactions. This disruption or alteration is potentially what leads to a decrease in the fraction of Nash pairs (α) over time in some of the system models.

Eventually, the system reaches an evolutionary stable state, characterized by stability and equilibrium in the strategies adopted by individuals. At this point, α stabilizes at its minimum value, possibly with minor fluctuations. This indicates that the system has settled into a relatively stable configuration where cooperative behavior is sustainable.

In contrast, if cooperators cannot survive in the system, α grows over time and approaches a value of 1, as observed in plot (A) of Figure 1 when T ≥ 1.5. This suggests a dominance of non-cooperative strategies, possibly leading to instability or unfavorable outcomes for individuals within the system. Once again, this is seen in Figure 3, where there is a stark increase in defectors when T ≥ 1.5.

**Figure 4: The comparison between α and β for T = 1.2 of the PDG**


### Extenstion



### Causes for Concern

One of the main causes for concern is the failure to perfectly replicate their results. The first caveat of our research is that while they ran their simulations for around 11,000 steps each, with each parameter sweep consisting of multiple repeated simulations just in case, we only did up to 500 timesteps and only did a simulation per parameter sweep. This means that we cannot fully confirm if our networks have reached a true evolutionary stable state as 500 timesteps are barely enough compared to 11,000 timesteps. The reason why we were not able to do 11,000 and take the average of multiple simulations was due to the time complexity of the program. While running 500 steps for 10 different simulations for WS graphs took around 7-9 minutes total, to simply run 10 simulations for 500 steps in BA graphs, it took on average 45-55 minutes. Given that it took that much to run the BA graphs, it did not seem feasible for us to go for 11,000 steps total. 

We chose 500 timesteps because when we looked at the research paper, it seemed that alpha had stabilized around the 500-1000 timestep mark. Hence, while we chose 500 as a reasonable compromise between runtime and accuracy to the original research conditions, it is important to acknowledge that the findings are not completely identical to the research paper. 

Furthermore, there were definitely some graphs that did not match picture perfect to the results of the Nash Equilibrium paper. This is also a cause of concern since most of the graphs seem to align with what we expected, but there are some unexplainable behaviors that we noticed.  

### Annotated Bibliography
[Local Nash Equilibrium in Social Networks](https://www.nature.com/articles/srep06224.pdf#:~:text=The%20local%20Nash%20equilibrium%20provides%20a%20way%20to,evolutionary%20stable%20state%20for%20the%20Prisoner%E2%80%99s%20dilemma%20game) **Yichao Zhang, M. A. Aziz-Alaoui, Cyrille Bertelle & Jihong Guan**
This paper investigated two different imperfect information games, The Prisoner’s Dilemma and the Snow Drift/Hawk-Dove/Chicken, and saw how an evolutionary stable state emerged (using local Nash equilibrium to measure) when these two games were placed in a small world (WS) and scale-free (BA) networks.
