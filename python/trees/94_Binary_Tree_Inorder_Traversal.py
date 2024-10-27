# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         # def inorder(root,output):
#         #     if root:
#         #         inorder(root.left,output)
#         #         output.append(root.val)
#         #         inorder(root.right,output)
#         #         return output
#         # output = []
#         # inorder(root,output)
#         # return output


#         res = []
#         if not root:
#             return res
        
#         stack = []
        
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right
#         return res 
    
import os

def create_multiple_files(filenames):
    for filename in filenames:
        with open(filename, 'w') as f:
            pass  # Create an empty file

if __name__ == '__main__':
    filenames = ['1448_Count_Good_Nodes_in_Binary_Tree.py', 
                 '230_Kth Smallest_Element_in_a_BST.py', 
                 '513_Find_Bottom_Left_Tree_Value.py',
                 ]
    create_multiple_files(filenames)