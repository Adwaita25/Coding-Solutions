# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
res = []
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            if not root:
                return
            inorderTraversal(root.left)
            res.append(root.val)
            inorderTraversal(root.right)
            
            return res
