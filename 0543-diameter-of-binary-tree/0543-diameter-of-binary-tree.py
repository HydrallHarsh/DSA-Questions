# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = -1
        def max_depth(root):
            if not root:
                return 0
            
            l = max_depth(root.left)
            r = max_depth(root.right)
            return max(l,r) + 1
        
        # return max_depth(root.left) + max_depth(root.right)

        
        def every_root(root,ans):
            if not root:
                return
            depth = max_depth(root.left) + max_depth(root.right)
            # print(depth, root.val)
            ans = max(depth,ans)
            # print("ans :", ans)
            a = every_root(root.left,ans)
            b = every_root(root.right,ans)
            if a and b:
                ans = max(ans, max(a,b))
            elif a :
                ans = max(ans, a)
            elif b:
                ans = max(ans, b)
            # print("ans after :", ans)
            return ans
        
        
        return every_root(root,ans)
    
