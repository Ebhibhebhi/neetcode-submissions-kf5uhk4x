class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            ix, iy = points[i]
            for j in range(i+1, N):
                jx, jy = points[j]

                dist = abs(ix - jx) + abs(iy - jy)
                
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algorithm
        minH = [[0, 0]]
        res = 0
        visit = set()

        while len(visit) != len(points):
            cost, p = heapq.heappop(minH)

            if p in visit:
                continue
            
            res += cost
            visit.add(p)

            for neiCost, nei in adj[p]:
                heapq.heappush(minH, [neiCost, nei])
        
        return res


        
            
                



