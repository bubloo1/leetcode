from typing import List,Optional
from collections import defaultdict
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, remainingTotal, nodeList):
            if not root:
                return 
           
            dfs(root.left, remainingTotal - root.val, nodeList + [root.val])
            dfs(root.right, remainingTotal - root.val, nodeList + [root.val])
            if root.left == None and root.right == None and not remainingTotal - root.val:
                nodeList.append(root.val)
                res.append(nodeList.copy())
            return res
                
        return dfs(root, targetSum, [])
    

newObject = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(newObject.pathSum(root,22))

