# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_lst = []
        q_lst = []
        for i in range(2):
            val = p.val if i == 0 else q.val
            curr = root
            s = []
            while curr.val != val:
                s.append(curr)
                if val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
            else:
                s.append(curr)
                if i == 0:
                    p_lst = s
                else:
                    q_lst = s

        small, big = p_lst, q_lst
        if len(q_lst) > len(p_lst):
            small, big = q_lst, p_lst
        
        big_set = set(big)

        for i in range(len(small)-1, -1, -1):
            if small[i] in big_set:
                return small[i]
        


