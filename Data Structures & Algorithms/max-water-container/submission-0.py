class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        for i in range(len(heights) - 1):
            j = i + 1
            while j < len(heights):
                curr = min(heights[i], heights[j]) * (j - i)
                water = max(water, curr)
                j+=1
        
        return water