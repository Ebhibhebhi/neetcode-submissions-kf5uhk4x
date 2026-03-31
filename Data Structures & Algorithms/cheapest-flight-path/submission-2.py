class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}

        for a1, a2, p in flights:
            adj[a1].append([p, a2])
        
        res = float("inf")
        minH = [[0,src,-1]]
        possible = False
        while minH:
            cost, a, stops = heapq.heappop(minH)

            if stops > k:
                continue
            
            if a == dst:
                return cost
                
            
            for c, nei in adj[a]:
                heapq.heappush(minH, [cost + c, nei, stops + 1])

        return -1
                
            
