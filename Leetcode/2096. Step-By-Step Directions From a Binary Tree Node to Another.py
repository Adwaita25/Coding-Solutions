# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(n: TreeNode, val: int, path: List[str]):
            if n.val == val:
                return True
            if n.left and dfs(n.left, val, path):
                path += 'L'
            elif n.right and dfs(n.right, val, path):
                path += 'R'
            return path
        source, dest = [], []
        
        dfs(root, startValue, source)
        dfs(root, destValue, dest)

        while len(source) and len(dest) and source[-1] == dest[-1]:
            source.pop()
            dest.pop()
        
        return "".join('U' * len(source)) + "".join(reversed(dest))
