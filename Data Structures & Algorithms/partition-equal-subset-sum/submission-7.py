class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        store = sum(nums)
        if store % 2 == 1:
            return False

        store//=2

        memoize = [[-1 for _ in range(len(nums))] for _ in range(store + 1)]

        def dfs(i, total):
            if total > store:
                return False
            if i == len(nums):
                return total == store
            if memoize[total][i]!= -1:
                return memoize[total][i]
            if total == store:
                memoize[total][i] = True
                return True
            
            memoize[total][i] = dfs(i + 1, total + nums[i]) or dfs(i+1, total)
            return memoize[total][i]
        
        return dfs(0,0)
            


        
            


        