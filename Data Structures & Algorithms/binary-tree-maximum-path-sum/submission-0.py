# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node, sum_sofar=float("-inf")):
            if not node:
                return float("-inf")
            
            nonlocal res
            if sum_sofar == float("-inf"):
                pass_down = node.val
            else:
                sum_sofar += node.val
                pass_down = max(sum_sofar, node.val)
            
            res = max(pass_down, res)

            left_tree_sum = dfs(node.left, pass_down)
            right_tree_sum = dfs(node.right, pass_down)

            res = max(res, left_tree_sum + right_tree_sum + node.val,
            pass_down + left_tree_sum, pass_down + right_tree_sum, node.val)

            pass_up = max(max(left_tree_sum, right_tree_sum)+node.val, node.val)
            return pass_up
        
        dfs(root)
        return res
