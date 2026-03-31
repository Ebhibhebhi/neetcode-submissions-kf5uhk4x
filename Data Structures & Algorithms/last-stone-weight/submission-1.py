class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_1 = heapq.heappop(heap)
            stone_2 = heapq.heappop(heap)
            if stone_1 < stone_2:
                heapq.heappush(heap, stone_1 - stone_2)
        
        return -heap[0] if heap else 0

            
