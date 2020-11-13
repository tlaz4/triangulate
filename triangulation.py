from enum import Enum
import random

# a enum class we can use to represent colors
class Color(Enum):
	RED = 1
	BLUE = 2
	YELLOW = 3

# our node class
# a node has a color, and also if it is a border node (colours cant change)
class Node:
	def __init__(self, name, color=None, is_border=False):
		self.color = color
		self.name = name

		if not self.color:
			self.is_border = False
		else:
			self.is_border = True

	def color_node(self, color):
		self.color = color

# a utility function to check if we have a complete triangle
def check_complete_triangle(triangle, nodes):
	if nodes[triangle[0]].color != nodes[triangle[1]].color != nodes[triangle[2]].color:
		return True
	else:
		return False

# a utility function to randomize all node colours
def randomize_node_colors(nodes):
	for node in nodes.values():
		if not node.is_border:
			new_color = Color(random.randint(1, 3))
			node.color_node(new_color)

# our main hillclimbing loop
def hillclimb():
	node_mapping = {
		'A': {'color': Color.RED, 'edges': ['K', 'L', 'B', 'V']},
		'B': {'color': Color.RED, 'edges': ['M', 'L', 'A', 'C']},
		'C': {'color': Color.YELLOW, 'edges': ['N', 'M', 'O', 'D', 'B']},
		'D': {'color': Color.BLUE, 'edges': ['P', 'O', 'C', 'E']},
		'E': {'color': Color.RED, 'edges': ['P', 'F', 'D']},
		'F': {'color': Color.RED, 'edges': ['P', 'Q', 'E', 'G']},
		'G': {'color': Color.YELLOW, 'edges': ['R', 'Q', 'F', 'H']},
		'H': {'color': Color.BLUE, 'edges': ['R', 'G', 'I']},
		'I': {'color': Color.RED, 'edges': ['R', 'T', 'S', 'H', 'J']},
		'J': {'color': Color.YELLOW, 'edges': ['S', 'K', 'I', 'V']},
		'V': {'color': Color.BLUE, 'edges': ['K', 'A', 'J']},
		'K': {'color': None, 'edges': ['S', 'T', 'L', 'A', 'V', 'J']},
		'L': {'color': None, 'edges' : ['K', 'T', 'U', 'M', 'B', 'A']},
		'M': {'color': None, 'edges': ['L', 'U', 'N', 'C', 'B']},
		'N': {'color': None, 'edges': ['M', 'U', 'O', 'C']}, 
		'O': {'color': None, 'edges': ['U', 'Q', 'P', 'D', 'C', 'N']},
		'P': {'color': None, 'edges': ['Q', 'F', 'E', 'D', 'O']},
		'Q': {'color': None, 'edges': ['R', 'G', 'F', 'P', 'O', 'U', 'T']},
		'R': {'color': None, 'edges': ['I', 'T', 'Q', 'G', 'H']},
		'S': {'color': None, 'edges': ['I', 'J', 'K', 'T']},
		'T': {'color': None, 'edges': ['I', 'S', 'K', 'L', 'U', 'Q', 'R']},
		'U': {'color': None, 'edges': ['Q', 'T', 'L', 'M', 'N', 'O']}
	}

	# all of our triangles arranged as the 3 nodes that make up the triangle
	triangles = [
		['A', 'B', 'L'],
		['B', 'C', 'M'],
		['M', 'N', 'C'],
		['C', 'O', 'N'],
		['C', 'O', 'D'],
		['O', 'P', 'D'],
		['P', 'D', 'E'],
		['P', 'F', 'E'],
		['P', 'Q', 'F'],
		['Q', 'F', 'G'],
		['Q', 'G', 'R'],
		['R', 'H', 'G'],
		['R', 'I', 'H'],
		['T', 'R', 'I'],
		['S', 'T', 'I'],
		['S', 'J', 'I'],
		['K', 'S', 'J'],
		['V', 'K', 'J'],
		['A', 'K', 'V'],
		['A', 'L', 'K'],
		['B', 'M', 'L'],
		['K', 'T', 'S'],
		['L', 'T', 'K'],
		['L', 'U', 'T'],
		['L', 'M', 'U'],
		['M', 'N', 'U'],
		['O', 'N', 'U'],
		['U', 'O', 'Q'],
		['O', 'P', 'Q'],
		['U', 'T', 'Q'],
		['Q', 'T', 'R']
	]

	non_edges = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U']

	# create all of our node objects from our node mappings using dictionary comprehension
	nodes = { node[0]: Node(node[0], color=node[1]['color']) for node in node_mapping.items() }
	randomize_node_colors(nodes)

	# keep track of our last count
	# and also the amount of tries we have had per this iteration
	# restarts so we know when to end
	last_count = 40
	tries = 0
	restarts = 0

	# we havent completed the goal so we keep looping 
	while True:
		count = 0

		# pick a random node that isnt an border node and assign it a random color
		# also keep the last colour of the node so we can revert it
		rand_node_int = random.randint(0, len(non_edges) - 1)
		rand_node = nodes[non_edges[rand_node_int]]
		rand_color = random.randint(1, 3)

		last_color = rand_node.color
		rand_node.color_node(Color(rand_color))


		# check how many complete triangles we have
		for triangle in triangles:
			if check_complete_triangle(triangle, nodes): 
				count += 1


		# if our count is better than last ie we have less triangles, keep the color change
		# else revert back
		if count < last_count:
			last_count = count
		else:
			rand_node.color_node(last_color)

		# if we reach 2 complete triangles, end the loop
		if count == 2:
			# if we have our solution, print the graph
			print("A solution exists! Here are the nodes and their respective colours")
			for node in nodes.values():
				print(node.name, node.color)

			break

		tries += 1

		# if we have tried n times, lets randomly assign new colours
		# if we go over the amount of restarts, we can assume that there is no solution
		# and the hillclimber has failed
		if tries == 20000:
			randomize_node_colors(nodes)

			restarts += 1

			if restarts > 5:
				print("No Solution Found")
				break

			tries = 0


def main():
	hillclimb()

if __name__ == '__main__':
	main()

