class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = nums[i] * - 1
            while j < k:
                if nums[k] + nums[j] == target:
                    mine = [nums[i], nums[j], nums[k]]
                    if  mine not in result:
                        result.append(mine)
                    j+=1
                    k-=1
                elif nums[k] + nums[j] > target:
                    k-=1
                else:
                    j+=1
        
        
        return result
            


