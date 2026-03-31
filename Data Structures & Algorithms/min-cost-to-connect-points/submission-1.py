class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            for j in range(i + 1, N):
                ix, iy = points[i]
                jx, jy = points[j]
                cost = abs(ix - jx) + abs(iy -jy)

                adj[i].append([cost, j])
                adj[j].append([cost, i])
        
        # Prim's algorithm

        res = 0
        minH = [[0,0]]
        visit = set()

        while len(visit) < N:

            c, p = heapq.heappop(minH)

            if p in visit:
                continue
            
            res += c
            visit.add(p)

            for neiCost, nei in adj[p]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res
            
                



