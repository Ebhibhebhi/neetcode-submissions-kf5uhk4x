class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        a = 0
        b = 0

        x = 0
        y = 0

        for i in range(1, len(nums)):
            tmp = max(nums[i] + a, b)
            a = b
            b = tmp
        
        x = b

        a = 0
        b = 0

        for i in range(2, len(nums)-1):
            tmp = max(nums[i] + a, b)
            a = b
            b = tmp
        
        y = b

        return max(nums[0] + y, x)

        