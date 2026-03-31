class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        a = 1
        b = 1

        for i in range(n):
            tmp = b
            b+=a
            a = tmp
        
        return a



        