from typing import List,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        leftToRight = True
        res = []
        while queue:
            lenOfQueue = len(queue)
            row = [0] * lenOfQueue

            for i in range(lenOfQueue):
                node = queue.popleft()
                # fill from right in row or left based on leftToRight
                index = i if leftToRight else (lenOfQueue - 1 - i) 
                row[index] = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            leftToRight = not leftToRight
            res.append(row)
        
        return res