# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bottomLeft = root.val

        def dfs(node, level, maxLevel):
            nonlocal bottomLeft
            if not node:
                return maxLevel

            if level > maxLevel:
                bottomLeft = node.val
                maxLevel = level

            maxLevel = dfs(node.left, level + 1, maxLevel)
            maxLevel = dfs(node.right, level + 1, maxLevel)
            return maxLevel

        dfs(root, 0, -1)
        return bottomLeft