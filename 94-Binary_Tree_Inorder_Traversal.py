# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result, stack = [], [root,]
        
        while stack:
            root = stack.pop()
            if root.left:
                tmp = copy.copy(root)
                tmp.left = None
                stack.append(tmp)
                stack.append(root.left)
            else:
                result.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
        return result
        