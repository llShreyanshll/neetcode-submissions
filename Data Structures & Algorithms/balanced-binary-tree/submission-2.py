# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True
        def dfs(root):
            nonlocal isBal

            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            if l - r > 1 or r - l > 1:
                isBal = False

            return 1 + max(l, r)
        dfs(root)
        return isBal

       