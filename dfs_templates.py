# Template 1 - Recursion

# Return true if there is a path from curr to target.

def DFS(curr: Optional[TreeNode], target: Optional[TreeNode], visited: set(Optional[TreeNode])) -> bool:
	if curr == target: return True
	for next_node in curr.next:
		if next_node not in visited:
			visited.add(next_node)
			if DFS(next_node, target, visited): return True
	return False


# Template 2 - explicit stack

# cons of using recursion: easy to implement
# pros of using recursion: when the depth of recursion is too high, it may become stack overflow ;(
# in this case, either using bfs or implementing dfs with explicit stack would be a solution

# Return true if there is a path from curr to target.

def DFS(root: int, target: int) -> bool:
	visited, stack = {}, []
	stack.append(root)
	while stack:
		curr = stack.pop()
		if curr == target: return True
		for next_node in curr.next:
			if next_node not in visited:
				visited.add(next_node)
				stack.append(next_node)
	return False