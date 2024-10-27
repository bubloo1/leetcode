# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # def postOrder(root,result):
        #     if root:
        #         postOrder(root.left,result)
        #         postOrder(root.right,result)
        #         result.append(root.val)
        #     return result
        # return postOrder(root,[])
        postOrder = []
        if not root:
            return postOrder

        s1 = []
        s2 = []
        s1.append(root)

        while s1:
            curr = s1.pop()
            s2.append(curr)

            if curr.left:
                s1.append(curr.left)

            if curr.right:
                s1.append(curr.right)

        while s2:
            postOrder.append(s2.pop().val)

        return postOrder