# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root, l):
            if not root:
                l.append(None)
                return
            
            l.append(root.val)
            traverse(root.left, l)
            traverse(root.right,l)
            return l

        l1 = traverse(p, [])
        l2 = traverse(q, [])
        print(l1,l2)
        if l1 == l2:
            return True
        else:
            return False