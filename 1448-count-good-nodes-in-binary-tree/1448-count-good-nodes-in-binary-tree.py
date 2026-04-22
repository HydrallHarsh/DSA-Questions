# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        currpath = []
        def dfs(root,path):
            nonlocal count
            if not root:
                return
            currpath.append(root.val)
            if max(currpath) <= root.val:
                count +=1
            dfs(root.left,currpath)
            dfs(root.right,currpath)
            if currpath:
                currpath.pop()
            
        dfs(root,currpath)
        
        return count

            
