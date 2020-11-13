My solution utilizes a a hillclimbing algorith, an attempt to find the optimal solution to the problem described. Unfortunately I was unable to find a solution with this approach.
I have first defined the graph into a node class, and a dictionary to map colours and edges to nodes, along with
a list of all triangles and the nodes that comprise them.
The main hillclimbing loop then randomly colours the center nodes, and iteratively makes random changes to nodes.
If the random change is found to have decreased the amount of complete triangles within the polygon, the change is accepted. Otherwise, the change is discared and a a new change is made. The hillclimbing algorithm depends on the initial solution, so throughout its run, the center nodes are all reandomly assigned a colour again if no solution can be found in the current iteration.

Resources:
	https://en.wikipedia.org/wiki/Hill_climbing
	https://www.python.org/doc/essays/graphs/
	https://en.wikipedia.org/wiki/Graph_coloring

This took me about 6 hours, including research and also an attempt to solve the puzzle by hand.

If I were to do this differently, I would rethink the algorithm I was using. I have been succesful with optimizing solutions in the past using hillclimbing, however I know that the algorithm can get stuck in a local optima, which I believe was the case here. Next time I would tackle the problem differently, and perhaps iterate through the solution space entirely to find the solution. I would also add unit tests if I had found a solution, to ensure that the complete triangles were in fact accurate, and the solution verified with testing.

To run the code from the command line, simply execute `python triangulation.py`


