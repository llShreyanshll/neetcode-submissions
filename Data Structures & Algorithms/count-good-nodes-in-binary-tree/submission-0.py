# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, cur_max):
            if not root:
                return None

            nonlocal res
            if root.val >= cur_max:
                res += 1
                cur_max = root.val
            
            left = dfs(root.left, cur_max)
            right = dfs(root.right, cur_max)
            

        dfs(root, float("-inf"))
        return res