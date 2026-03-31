class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i:[] for i in range(1, n+1)}

        for source, target, time in times:
            adj[source].append([time, target])
        
        minheap = []
        visit = set()

        heapq.heapify(minheap)
        heapq.heappush(minheap, [0, k])
        
        res = 0

        while minheap:
            
            t, node = heapq.heappop(minheap)
            
            if node in visit:
                continue
            
            res = t
            
            visit.add(node)

            for nei in adj[node]:
                t2, node2 = nei
                heapq.heappush(minheap, [t2 + t, node2])

        return res if len(visit) == n else -1

        







