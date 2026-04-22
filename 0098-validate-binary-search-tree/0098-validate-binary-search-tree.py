# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,l,h):
            if not root:
                return True
            if not( l < root.val and h > root.val):
                return False

            a = dfs(root.left, l, root.val)
            b = dfs(root.right, root.val, h)

            return a and b
    
        return dfs(root, float('-inf'), float('inf'))
        

        