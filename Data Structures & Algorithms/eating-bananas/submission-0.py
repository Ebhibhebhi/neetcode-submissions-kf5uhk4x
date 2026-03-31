class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        
        while l <= r:
            t = 0
            k = (r + l)//2
            for pile in piles:
                t+= pile//k
                if pile%k != 0:
                    t+=1
            
            if t > h:
                l = k + 1
            
            else:
                res = k
                r = k - 1
            
        return res





            
