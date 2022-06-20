from collections import deque

# Template 1

# Return the length of the shortest path between root and target node.
def BFS(root, target):
	queue = deque()
	step = 0
	# initialize
	queue.append(root)
	# BFS
	while queue:
		# initialize the nodes which are already in the queue
		size = len(queue)
		for i in range(size):
			curr = queue.popleft()
			if curr == target: return step
			queue.append(curr.next)
		step += 1
	return -1


# Template 2
# never visit a node twice

def BFS(root, target):
	queue, visited = deque(), deque()
	setp = 0
	# initialize
	queue.append(root)
	visited.append(root)
	# BFS
	while queue:
		# iterate the nodes which are already in the queue
		size = len(queue)
		for i in range(size):
			curr = queue.popleft()
			if curr = target: return step
			for node in next:
				if node not in visited:
					queue.append(node)
					visited.append(node)
		step += 1
	return -1
