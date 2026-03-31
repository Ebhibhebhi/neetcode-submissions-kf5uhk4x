class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * n

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if cache[i-1] != -1:
                return cache[i-1]
            
            a = dfs(i + 1)
            cache[i] = a
            b = dfs(i + 2)
            if i + 1 < n:
                cache[i+1] = b

            return a + b
        
        return dfs(0)



        