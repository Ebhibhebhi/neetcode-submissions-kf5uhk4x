class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            result = [0] * len(nums)
            for i in range(len(nums)):
                if i != nums.index(0):
                    product*=nums[i]
            result[nums.index(0)] = product
            return result
        
        product = 1
        for i in range(len(nums)):
            product*=nums[i]
        result = []
        for i in range(len(nums)):
            result.append(product//nums[i])
        return result