class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            tmp = max(nums[i] + a, b)
            a = b
            b = tmp
        
        return b

        