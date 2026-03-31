# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, left_b, right_b):
            if not root:
                return True
            if not (root.val < right_b and root.val > left_b):
                return False
            
            return isValid(root.left, left_b, root.val) and isValid(root.right, root.val, right_b)
        
        return isValid(root, float("-inf"), float("inf"))
