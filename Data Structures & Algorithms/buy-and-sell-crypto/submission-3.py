class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        increases = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                increases+=1
        if increases == 0:
            return 0
        elif increases == len(prices) - 1:
            return (prices[len(prices)-1] - prices[0])
        
        n = 0
        while n < len(prices) - 1:
            if prices[n+1] == prices[n]:
                del prices[n+1]
            n+=1

        maxdict = {
            0 : prices[0],
            len(prices) - 1 : prices[len(prices) - 1]
        }

        mindict = {
            0 : prices[0],
            len(prices) - 1 : prices[len(prices) - 1]
        }

        for i in range(1, len(prices)-1):
            if prices[i-1] < prices[i] and prices[i+1] < prices[i]:
                maxdict[i] = prices[i]
            elif prices[i-1] > prices[i] and prices[i+1] > prices[i]:
                mindict[i] = prices[i]
            
        profit = 0

        for mindex, Min in mindict.items():
            for madex, Max in maxdict.items():
                if madex > mindex:
                    profit = max(profit, Max - Min)
        
        return profit

        











