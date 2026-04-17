class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        
        def dfs(r):
            if r is None:
                return 0
            
            left = dfs(r.left)
            right = dfs(r.right)
            if abs(left - right) > 1:
                self.res = False
            
            return 1 + max(left, right)

        dfs(root)
        return self.res