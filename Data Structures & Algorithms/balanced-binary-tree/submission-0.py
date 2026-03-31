# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.state = True
        
        def dfs(root):
            if not root:
                return 0
            
            height_r = dfs(root.right)
            height_l = dfs(root.left)

            if height_r == "false" or height_l == "false":
                return "false"

            if abs(height_r - height_l) > 1:
                self.state = False
                return "false"
            
            return max(height_r, height_l) + 1
        
        dfs(root)
        return self.state


