# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        a = [root]
        queue.append(a)
        if root:
            ans = [root.val]
        else:
            return []
        while queue:
            node = queue.popleft()
            # print(type(node))
            temp = []
            for i in node:
                # print(i)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                # print("Temp:", temp)

            if len(temp) != 0:
                queue.append(temp) 
            else:
                continue
            ans.append(temp[-1].val)
        return ans