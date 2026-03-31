class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i:[] for i in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append([v,w])
        
        minH = [[0, k]]
        visit = set()
        res = 0

        while minH:
            t, node = heapq.heappop(minH)
            if node in visit:
                continue
            
            visit.add(node)
            res = max(res, t)

            for nei, w in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH, [w + t, nei])
        
        return res if len(visit) == n else -1
            


        







