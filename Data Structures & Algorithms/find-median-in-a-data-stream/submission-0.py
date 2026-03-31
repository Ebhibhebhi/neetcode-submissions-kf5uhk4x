class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)

        if self.minh and (-self.maxh[0] > self.minh[0]):
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        
        diff = len(self.maxh) - len(self.minh)
        # if diff is positive self.maxh is bigger otherwise self.maxh is bigger
        if (abs(diff) > 1):
            if diff > 0:
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
            else:
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
    
    def findMedian(self) -> float:
        if len(self.maxh) < len(self.minh):
            return self.minh[0]
        if len(self.minh) < len(self.maxh):
            return -self.maxh[0]

        return (self.minh[0] + (-self.maxh[0]))/2
        
        
        """

        """