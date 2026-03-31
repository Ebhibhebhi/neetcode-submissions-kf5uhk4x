class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []

        for i in range(k):
            window.append(nums[i])
        
        res = [max(window)]
        l, r =  0, k - 1
        
        while r < len(nums) - 1:
            window.remove(nums[l])
            l+=1
            r+=1

            window.append(nums[r])
            res.append(max(window))
        
        return res
