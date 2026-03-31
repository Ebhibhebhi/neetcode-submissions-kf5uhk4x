class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(decision):
            if decision == len(nums):
                res.append(subset.copy())
                return
            
            dfs(decision+1)
            subset.append(nums[decision])
            dfs(decision+1)
            subset.pop()
        
        dfs(0)
        
        return res
