from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.prev = None
        self.min_diff = float('inf')
        
        def dfs(node):
            if not node:
                return
            
            # In-order traversal: Left -> Node -> Right
            dfs(node.left)
            
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            dfs(node.right)
        
        dfs(root)
        return self.min_diff

        # BFS traversal to collect all node values
        # queue = deque([root])
        # values = []
        
        # while queue:
        #     node = queue.popleft()
        #     values.append(node.val)
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        
        # Sort the values and find the minimum absolute difference
        # values.sort()
        # return min(values[i] - values[i-1] for i in range(1, len(values)))
