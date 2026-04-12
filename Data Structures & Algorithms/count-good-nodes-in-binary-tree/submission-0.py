# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        max_node = -float("inf")

        def dfs(node, max_node):
            nonlocal count

            if not node:
                return
            
            if max_node <= node.val:
                max_node = node.val
                count += 1

            dfs(node.left, max_node)    
            dfs(node.right, max_node)
        
        dfs(root, max_node)

        return count
        