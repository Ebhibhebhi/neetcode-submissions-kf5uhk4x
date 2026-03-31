class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            else:
                my_set.add(nums[i])
        else:
            return False