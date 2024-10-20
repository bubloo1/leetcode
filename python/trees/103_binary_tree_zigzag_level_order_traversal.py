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
        result = []
        if not root:
            return result

        nodes_queue = deque([root])
        left_to_right = True

        while nodes_queue:
            size = len(nodes_queue)
            row = [0] * size

            for i in range(size):
                node = nodes_queue.popleft()

                # find position to fill node's value
                index = i if left_to_right else (size - 1 - i)

                row[index] = node.val
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)

            # after this level
            left_to_right = not left_to_right
            result.append(row)

        return result