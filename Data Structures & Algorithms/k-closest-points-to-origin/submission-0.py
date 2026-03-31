class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [math.sqrt((pt[0]**2)+(pt[1]**2)) for pt in points]
        heap = distances.copy()
        heapq.heapify(heap)
        res = []
        for i in range(k):
            index = distances.index(heapq.heappop(heap))
            res.append(points[index])
            distances[index] = -1


        return res