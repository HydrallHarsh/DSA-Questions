# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def traverse_2(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            l = traverse_2(root.left, subroot.left)
            r = traverse_2(root.right, subroot.right)
            return l and r
            
        def traverse(root, subroot):
            if not root:
                return False
            temp = False
            if traverse_2(root, subroot):
                return True

            a = traverse(root.left, subroot)
            b = traverse(root.right , subroot)
            return a or b

        return traverse(root, subRoot)
            