class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, unused):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(unused) - 1, -1, -1):
                curr.append(unused[i])
                dfs(curr, unused[:i] + unused[i+1:])
                curr.pop()
        
        dfs([], nums.copy())

        return res

                