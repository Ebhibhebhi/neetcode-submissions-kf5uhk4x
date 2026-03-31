class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(len(edges) + 1)}

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        

        def dfs(node, target, parent, visit):
            if node == target:
                return True
            
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, target, node, visit):
                    return True
            visit.remove(node)
            return False
        
        for i in range(len(edges) - 1, -1, -1):
            
            n1, n2 = edges[i]
            
            if dfs(n2, n1, n1, set()):
                return edges[i]

            

