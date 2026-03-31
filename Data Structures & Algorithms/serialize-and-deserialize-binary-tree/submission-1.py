# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        my_list = []

        def dfs(node):
            nonlocal my_list
            if not node:
                my_list.append("n")
                return
            
            my_list.append(node.val)
            
            dfs(node.left)
            dfs(node.right)

            return ",".join(str(x) for x in my_list)

        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        vals = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if vals[i] == "n":
                i+=1
                return None
            
            node = TreeNode(int(vals[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()













