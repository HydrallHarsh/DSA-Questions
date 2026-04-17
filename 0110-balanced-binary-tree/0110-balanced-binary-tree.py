# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(root):
            if not root:
                return 0
            
            l = max_depth(root.left)
            r = max_depth(root.right)
            return max(l,r) + 1
        

        def dfs(root):
            if not root:
                return True
            
            diff = abs(max_depth(root.left) - max_depth(root.right))
            if diff > 1:
                return False
        
            a  = dfs(root.left)
            b = dfs(root.right)
            return a and b
        
        return dfs(root)
            


            