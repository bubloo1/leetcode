# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # output = []
        # def preOrder(root,output):
        #     if root:
        #         output.append(root.val)
        #         preOrder(root.left,output)
        #         preOrder(root.right,output)
        #     return output
        # return preOrder(root,output)
    
        if not root:
          return root
        res = []
        q = []
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.pop()
                res.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res
        

        