class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][-1]:
                res[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index, value])
        
        return res