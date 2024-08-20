from typing import Optional
from collections import deque
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

        # def bfs(root):

        #     queue = deque([root])
        #     bottomLeft = None
        #     while queue:
        #         node = queue.popleft()
        #         bottomLeft = node.val

        #         if node.right:
        #             queue.append(node.right)

        #         if node.left:
        #             queue.append(node.left)
        #     return bottomLeft
        # return bfs(root)


newTreeObj = TreeNode(1)
newTreeObj.left = TreeNode(2)
newTreeObj.right = TreeNode(3)
newTreeObj.left.left =TreeNode(4)
newTreeObj.right.left = TreeNode(5)
newTreeObj.right.right = TreeNode(6)
newTreeObj.right.left.left = TreeNode(7)

newObject = Solution()

print(newObject.findBottomLeftValue(newTreeObj))