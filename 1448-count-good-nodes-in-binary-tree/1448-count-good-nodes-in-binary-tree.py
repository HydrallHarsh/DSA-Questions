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
        maps = {}
        gmax = 0
        def dfs(root,path):
            nonlocal count
            if not root:
                # if currpath:
                #     currpath.pop()
                return
            # if gmax =
            currpath.append(root.val)
            maps[tuple(currpath)] = max(currpath)
            # print(root.val, currpath, maps)
            if maps[tuple(currpath)] <= root.val:
                print("i am in")
                count +=1
            # if root.val > max()
            dfs(root.left,currpath)
            dfs(root.right,currpath)
            if currpath:
                currpath.pop()
            # return count
            
        dfs(root,currpath)
        
        return count

            
