# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.revisited = set()
        self.res = root.val

        def dfs(node, k, found):
            if found:
                return
            if not node:
                return

            dfs(node.left, k, found)
            self.revisited.add(node.val)
            if len(self.revisited) == k:
                self.res = node.val
                found = True
            dfs(node.right, k, found)

        dfs(root, k, False)
        return self.res
        
        

        

