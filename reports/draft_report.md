# Investigating Nash Equilibrium in Social Networks through the Prisoner’s Dilemma Game:
# A Replication Study and Analysis of Simulation Results

By: Trinity Lee and Daniel Quinteros

## 1) An abstract that identifies the topics you are investigating and the tools you are using.

Our goal for the project was to investigate the local Nash Equilibrium phenomenon in social networks by simulating the Prisoner’s Dilemma Game. These simulations integrated two types of networks: Watts and Strogatz small-world networks (WS) and Barabasi and Albert scale-free networks (BA). We utilized the Python network tool created by Allen Downey for that purpose.

## 2) An annotated bibliography of papers that relate to your topic and/or tools.  Explain what the papers are about, what experiments they report, and what their primary conclusions are.

The main paper we referenced for our project was called ["Local Nash Equilibrium in Social Networks"](https://www.nature.com/articles/srep06224.pdf#:~:text=The%20local%20Nash%20equilibrium%20provides%20a%20way%20to,evolutionary%20stable%20state%20for%20the%20Prisoner%E2%80%99s%20dilemma%20game).This paper investigated two different imperfect information games, The Prisoner’s Dilemma and the Snow Drift/Hawk-Dove/Chicken, and saw how an evolutionary stable state emerged (using local Nash equilibrium to measure) when these two games were placed in a small world (WS) and scale-free (BA) networks. The paper measured the percentage of Nash pairs (two agents who reached Nash equilibrium with each other) within a network and the frequency of cooperators (a potential outcome role within each game) in the entire system.

For the purposes of our project, we mainly focused on their methodologies and findings in regards to the Prisoner’s Dilemma Game (PDG). In the Prisoner’s Dilemma Game, there were two strategies/roles an agent could choose: Cooperator or Defector.
For the PDG, the authors defined 4 parameters that influenced agent-based behavior: T (temptation to defect) for defecting a cooperator R (reward for mutual cooperation) for cooperating with a cooperator P (punishment for mutual defection) for defecting a defector S (sucker’s payoff) for cooperating with a defector.

Furthermore, they generated several mathematical representations of the different laws used to dictate agent behavior throughout this simulation. For updating these laws per timestep, they utilized two different approaches, Nowak & May and Santos & Pachecos.

Throughout the simulation, the number of Nash pairs and number of cooperators & defectors were kept track of to understand what was the best personal strategy for survival given different parameter values, networks, and update laws.

They used Local Nash equilibrium to judge whether a gaming structured population reached the evolutionary stable state and predicted whether cooperation could exist in a system long before the system reached its evolutionary stable state. Their model provided a potential explanation as to why the system exhibited a relatively stable state when the number of local Nash equilibriums reached the minimum. For the PDG, they found that once the fraction of Nash pairs in the connected individuals decayed with time, cooperators could survive in its evolutionary stable state. If cooperators could survive in the system, the system reached its evolutionary stable state when the fraction of Nash pairs reached its minimum. This was because these Nash pairs actually protected cooperative behavior. If all the defectors were in Nash pairs, then it cut these defectors’ payoffs and enabled cooperation to survive in a circumstance with a large temptation to defect. Overall, the paper proved that a local Nash equilibrium was a typical feature of the cooperative structured populations.

## 3) A description of the experiment from these papers that you are replicating and the extensions or variations of those experiments you are working on.

Our team reproduced the experiment examining the conditions under which a system reaches the evolutionary stable state when individuals play the Prisoner’s Dilemma game. The experiment’s variables include the type of network being used (WS or BA), the values assigned to the four parameters that influence agent-based behavior, and the updating rule utilized.

## 4) Results from the replication and possibly preliminary results from the extension. Or if you don't have results, sketch what the results from these experiments might look like, possibly using a cartoon of a graphical result.

![Figure 1](https://github.com/tlee10333/NashEquilibrium/assets/47285707/c051c0fe-699e-4b0b-a5b5-4e04b4cbc3b0 "Figure 1")

Figure 1: The evolution of α, representing the fraction of Nash pairs in the connected individuals, for the PDG in social networks. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

![Figure 2](https://github.com/tlee10333/NashEquilibrium/assets/47285707/b65cd2cc-dd35-4b79-a014-a63a1388c5b5 "Figure 2")

Figure 2: The evolution of β, representing the proportion of cooperators within the entire population of players at a particular round (n) of the game. We performed a parameter sweep to investigate the impacts of changing the temptation to defect, ranging from T = 1.1 to T = 2.0, on the system. The remaining parameters of the PDG are fixed at P = S = 0, and R = 0.4.

## 5) Interpret the results; for example, "If the power spectrum on a log-log scale is approximately linear, we will estimate its slope.  If that slope is near 1, we will conclude that the time series generated by the model resembles pink noise."

In Figure 1, the decay of α is prevalent for the temptation to defect T < 1.5 in (a), T < 1.4 in (b), T < 1.9 in (c) and T < 2.0 in (d). Conversely, α stabilizes at a high value above the mentioned threshold values. In these instances, our simulation findings for β in Figure 2 indicate that cooperators can persist in the corresponding states.

None of our models managed to achieve a stabilization point at α = 1. Instead, they stabilized at a minimum level with slight fluctuations. Seeing as cooperators can survive in the system, it implies that cooperative behavior is sustainable and beneficial for individuals within the system. Consequently, one would expect to observe an increasing presence of cooperators within the Nash pairs over time, indicating their successful engagement and influence on other individuals. Having said that, this would mean that the introduction of cooperators possibly disrupts existing equilibria or alters the dynamics of interactions. This disruption or alteration is potentially what leads to a decrease in the fraction of Nash pairs (α) over time in some of the system models.

Eventually, the system reaches an evolutionary stable state, characterized by stability and equilibrium in the strategies adopted by individuals. At this point, α stabilizes at its minimum value, possibly with minor fluctuations. This indicates that the system has settled into a relatively stable configuration where cooperative behavior is sustainable.

In contrast, if cooperators cannot survive in the system, α grows over time and approaches a value of 1, as observed in some of our models. This suggests a dominance of non-cooperative strategies, possibly leading to instability or unfavorable outcomes for individuals within the system.

## 6) Identify causes for concern.  Review the criteria for what makes a good project and identify any areas where your project might be problematic.

One of the main causes for concern is the failure to perfectly replicate their results. The first caveat of our research is that while they ran their simulations for around 11,000 steps each, with each parameter sweep consisting of multiple repeated simulations just in case, we only did up to 500 timesteps and only did a simulation per parameter sweep. This means that we cannot fully confirm if our networks have reached a true evolutionary stable state as 500 timesteps are barely enough compared to 11,000 timesteps. The reason why we were not able to do 11,000 and take the average of multiple simulations was due to the time complexity of the program. While running 500 steps for 10 different simulations for WS graphs took around 7-9 minutes total, to simply run 10 simulations for 500 steps in BA graphs, it took on average 45-55 minutes. Given that it took that much to run the BA graphs, it did not seem feasible for us to go for 11,000 steps total. 

We chose 500 timesteps because when we looked at the research paper, it seemed that alpha had stabilized around the 500-1000 timestep mark. Hence, while we chose 500 as a reasonable compromise between runtime and accuracy to the original research conditions, it is important to acknowledge that the findings are not completely identical to the research paper. 

Furthermore, there were definitely some graphs that did not match picture perfect to the results of the Nash Equilibrium paper. This is also a cause of concern since most of the graphs seem to align with what we expected, but there are some unexplainable behaviors that we noticed.  

## 7) Outline next steps.  For each team member, what do you plan to work on immediately?  For the team, what do you think you can get done in the next week?  Consider using GitHub Projects to make a kanban board to track tasks.

Both:
- Revisualize the results graphs to make them easier to digest
- Explore more results interpretations
- Clean and comment the code each of us wrote
- Continue working on any extensions we believe are manageable given our time frame
- Possibly organize our code into a Jupiter notebook




