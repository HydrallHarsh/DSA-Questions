# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # root = preorder[0]
        # tree.val = root
        # for i, j in enumerate(zip(preorder,inorder)):
            
        #     # print(i,j[0])
        #     root = j[0]
        #     tree = Treenode(val, )
        #     tree.left = 
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])

        return root


        