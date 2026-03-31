# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            height_l = dfs(root.left)
            height_r = dfs(root.right)

            self.res = max(self.res, height_l + height_r)
            
            return max(height_l, height_r) + 1
        dfs(root)
        return self.res