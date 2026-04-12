# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        
        def dfs(node, val):
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                else:
                    dfs(node.right, val)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                else:
                    dfs(node.left, val)
        
        dfs(root, val)

        return root
