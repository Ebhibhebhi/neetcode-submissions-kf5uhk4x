class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1

        while numbers[a] + numbers[b] != target:
            if numbers[b] > (target - numbers[a]):
                b-=1
            else:
                a+=1
        
        return [a+1,b+1]
            