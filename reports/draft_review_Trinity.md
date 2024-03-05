# Draft Review

## Question

From what I understand, they are using a Biham-Middleton-Levine (BML) model in Cellular Automata to simulate traffic jamming. The two parameters they can choose are density of alive/on cells, and the size of the grid. They did a parameter sweep on the density of cells to see what density leads to jamming (aka the cells can't move)
## Methodology
The implement the BML model where cells are generated randomly with a 50/50 chance of moving to the right (blue) or moving down (red). Each cells moves in timestep if there isn't another cell blocking their way. 

From what I understand, they did a successful parameter sweep and jamming occurs at a density from 0.35 to 4. They also did a parameter sweep for size of grid but they found no impact on that. I think that it makes sense, though I'd like to have seen a graph showing the parameter sweep. 
## Results
The results are slightly confusing since they have the graphs all grouped together, though I can get the general gist of it. It would be nice if it had captions or it was organized by category. For example, I don't know what the difference between the left and right graphs are, though I can tell the difference between the first and second row of graphs if that makes sense. I'm assuming you just made the graphs move visually interpretable?

## Interpretation
I'd say so! It looks pretty valid and it makes sense intuitively. The only thing I'd say is that the conclusion could probably be better used to help with the interpretation. Right now it has a very "We replicated it! Hurray" feeling which is fine but it would be nice if they wrote some more in terms of reflection about their results. 

## Replication
I really can't tell you. The first 2 links forwarded me to a mysterious russian site. The last one didn't have any graphs to base off visually. 
## Extension
I think the extension is an interesting concept but I don't really see another new conceptual or structural extension project. It's more like they added a little twist to their current simulation and it just reinforced their idea that jams slow traffic down. I feel like there would definitely be more ways to further explore the topic. 

## Progress
I think so, just needs a better writeup/presentation of data and maybe a more intriguing extension. 
## Presentation
I wouldn't really comment on this yet, since this is clearly a draft. 
## Mechanics
I think it is! Hits all the basic requirements and has a really nice annotated biliography. 
