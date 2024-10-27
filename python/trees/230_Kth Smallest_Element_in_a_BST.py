# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(root,output):
            if not root:
                return
            
            dfs(root.left,output)
            output.append(root.val)
            dfs(root.right,output)
   
            return output
        return dfs(root,[])[k-1]