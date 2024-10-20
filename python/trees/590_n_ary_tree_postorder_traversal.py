# Definition for a Node.
from typing import Optional,List
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(node):
            if not node:
                return 

            for c in node.children:
                helper(c)
            res.append(node.val)

        helper(root)
        return res    
        