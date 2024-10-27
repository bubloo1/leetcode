# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root,level,output):
            
            if not root:
                return

            if level == len(output):
                output.append(root)
            
            dfs(root.right,level + 1,output)
            return output
        return dfs(root,0,[])

