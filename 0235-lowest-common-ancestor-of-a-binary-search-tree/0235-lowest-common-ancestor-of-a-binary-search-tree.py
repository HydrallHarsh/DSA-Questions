# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target,l):
            if not root or target in l:
                return l
            
            if root.val == target:
                l.append(root)
                return l
            l.append(root)
            if target < root.val :
                dfs(root.left,target,l)
            
            if target > root.val:
                dfs(root.right, target, l)
            return l
        l1 = dfs(root, p.val, [])
        l2 = dfs(root, q.val, [])
        smaller_len = min(len(l1),len(l2))
        if len(l1)<= len(l2):
            for i in range(smaller_len-1, -1, -1):
                if l1[i] == l2[i]:
                    return l1[i]
        else:
            for i in range(smaller_len-1, -1,-1):
                if l2[i] == l1[i]:
                    return l2[i]
         
        