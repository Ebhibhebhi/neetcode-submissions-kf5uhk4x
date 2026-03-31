class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       my_map = {}

       for i in range(len(nums)):
            t = target - nums[i]
            if t in my_map:
                return [my_map[t], i]
            my_map[nums[i]] = i
        




        
