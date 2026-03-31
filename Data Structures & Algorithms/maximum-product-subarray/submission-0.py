class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        arr = []
        for i in range(len(nums)-1, -1, -1):
            product = 1
            for i in range(i, len(nums)):
                product*= nums[i]
                res = max(res, product)

        return res
