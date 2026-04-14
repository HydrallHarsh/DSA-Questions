# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(root):
            if not root:
                return 0
            
            l = max_depth(root.left)
            r = max_depth(root.right)
            return max(l,r) + 1

        return max_depth(root)