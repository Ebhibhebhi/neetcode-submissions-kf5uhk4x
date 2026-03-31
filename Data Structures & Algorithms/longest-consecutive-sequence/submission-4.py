class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        result = 1
        a = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                a+=1
            elif nums[i + 1] == nums[i]:
                continue
            elif a > result:
                result = a
                a = 1
            else:
                a = 1
        if a > result:
            result = a
        return result
                



