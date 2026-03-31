class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjacent = {i : [] for i in range(n)}

        for i, j in edges:
            adjacent[i].append(j)
            adjacent[j].append(i)

        visit = set()

        def dfs(node, back):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjacent[node]:
                if nei == back:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
