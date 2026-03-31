class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in numSet:
                a = 1
                while num + a in numSet:
                    a+=1
                result = max(result, a)

        return result
                    




