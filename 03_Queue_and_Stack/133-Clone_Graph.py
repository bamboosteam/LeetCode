"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        stack, visited = [], []
        ans = Node()
        
        stack.append(node)
        while stack:
            curr = stack.pop()
            print(type(curr))
            return
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)        