class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]

        heapq.heapify(maxheap)

        while len(maxheap) > 1:

            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)

            if s1 < s2:
                heapq.heappush(maxheap, s1 - s2)

        
        return 0 if not maxheap else -maxheap[0]
        

            
