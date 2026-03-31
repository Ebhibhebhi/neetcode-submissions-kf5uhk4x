class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[(pt[0]**2)+(pt[1]**2), pt[0], pt[1]]  for pt in points]
        heapq.heapify(distances)
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            res.append([x,y])
        return res