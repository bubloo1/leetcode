from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            nonlocal res
            if not node:
                return
            
            if low <= node.val <= high:
                res += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
                
        res = 0
        dfs(root)
        return res
    
        # def preOrder(root):
        #     if not root:
        #         return 0
        #     res = 0
        #     res += preOrder(root.left)
        #     res += preOrder(root.right)
            
        #     if root.val >= low and root.val <= high:
        #         res += root.val
        #     return res
        # return preOrder(root)

ll = TreeNode(10)
ll.left = TreeNode(5)
ll.right = TreeNode(15)
ll.left.left = TreeNode(3)
ll.left.right = TreeNode(7)
ll.right.right = TreeNode(18)

newObject = Solution()
print(newObject.rangeSumBST(ll,7,15))