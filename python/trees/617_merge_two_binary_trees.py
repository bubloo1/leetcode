from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return None

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        root = TreeNode(val1 + val2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None)
        return root
        

        # if not root1:
        #     return root2
        
        # queue = deque([(root1, root2)])
        # while queue:

        #     # Pop the current nodes from the queue
        #     node1, node2 = queue.popleft()

        #     # If either node is None, continue to the next iteration
        #     if not node1 or not node2:
        #         continue

        #     # Update the value of the first tree node
        #     node1.val = node1.val + node2.val

        #     if not node1.left:
        #         # If the left child of the first tree node is None, assign it from the second tree
        #         node1.left = node2.left
        #     else:
        #         # Append both right children to the queue
        #         queue.append((node1.left, node2.left))

        #     if not node1.right:
        #         # If the right child of the first tree node is None, assign it from the second tree
        #         node1.right = node2.right
        #     else:
        #         # Append both right children to the queue
        #         queue.append((node1.right, node2.right))

        # # Return merged tree
        # return root1