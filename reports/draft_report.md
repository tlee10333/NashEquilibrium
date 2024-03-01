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

