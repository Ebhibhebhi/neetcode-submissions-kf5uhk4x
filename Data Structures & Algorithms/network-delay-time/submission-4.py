class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i:[] for i in range(1, n+1)}

        for u, v, t in times:
            adj[u].append([t, v])
        
        visit = set()
        minH = [[0,k]]
        res = 0

        while minH:
            t, node = heapq.heappop(minH)
            if node in visit:
                continue
            
            visit.add(node)
            res = max(res, t)

            for cost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH, [cost+t, nei])
        
        return res if len(visit) == n else -1
                

        
            


        







