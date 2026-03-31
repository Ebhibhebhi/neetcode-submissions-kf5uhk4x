class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(i, amt):
            if (i, amt) in cache:
                return cache[(i, amt)]
            
            if amt == 0:
                return 0
            
            if amt < 0 or i >= len(coins):
                return float("inf")

            cache[(i, amt)] = min(1 + dfs(i, amt - coins[i]), dfs(i+1, amt))

            return cache[(i, amt)]
        
        res = dfs(0, amount)

        return res if res != float("inf") else -1


