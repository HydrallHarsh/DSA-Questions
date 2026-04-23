# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []
        def dfs(root, path):
            if not root:
                return
            
            if len(path) == k:
                return path[-1]
            a = dfs(root.left, path)
            # if len(path) >= k:

            path.append(root.val)
            if len(path) == k:
                return path[-1]

            b = dfs(root.right, path)

            if a is not None:
                return a
            if b is not None:
                return b
            # print(a, b, path)

        return dfs(root, path)