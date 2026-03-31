class Solution:
    def climbStairs(self, n: int) -> int:
        ones = n
        twos = 0

        res = 0

        while ones >= 0:
            
            res += (math.factorial(ones + twos))/(math.factorial(ones) * math.factorial(twos))

            ones -= 2
            twos += 1

        return int(res)