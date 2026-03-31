class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n

        def find_root(node):
            curr = node
            while curr != parent[curr]:
                curr = parent[parent[curr]]
            return curr
        
        def union(n1, n2):
            r1, r2 = find_root(n1), find_root(n2)

            if r1 == r2:
                return 0
            
            if size[r1] > size[r2]:
                parent[r2] = r1
                size[r1] += 1
                return 1
            else:
                parent[r1] = r2
                size[r2] += 1
                return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)     
        
        return res


            
        
            
                
                
                