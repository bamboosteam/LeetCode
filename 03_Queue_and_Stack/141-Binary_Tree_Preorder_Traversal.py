# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        result = []
        right = []
        curr = root
        
        while curr:
            result.append(curr.val)
            if curr.left == None and curr.right == None and not right:
                break
            if curr.right != None:
                right.append(curr.right)
                
            if curr.left != None:
                curr = curr.left
                continue                
            elif curr.left == None:
                curr = right.pop()
                
        return result


# Solution 1
# class Solution(object):
#     def preorderTraversal(self, root):
#         if root is None:
#             return []

#         stack, output = [root, ], []

#         while stack:
#             root = stack.pop()
#             if root is not None:
#                 ourput.append(root.val)
#                 if root.right is not None:
#                     stack.append(root.right)
#                 if root.left is not None:
#                     stack.append(root.left)

#         return output