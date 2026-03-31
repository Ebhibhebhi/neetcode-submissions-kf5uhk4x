class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low1 = 0
        high1 = len(matrix) - 1
        mid1 = -1
        while low1 <= high1:
            mid1 = (high1 + low1)//2
            if matrix[mid1][0] <= target <= matrix[mid1][len(matrix[0]) - 1]:
                low2, high2 = 0, len(matrix[0]) - 1
                mid2 = -1

                while low2 <= high2:
                    mid2 = (high2 + low2)//2
                    if matrix[mid1][mid2] == target:
                        return True
            
                    elif matrix[mid1][mid2] < target:
                        low2 = mid2 + 1
            
                    else:
                        high2 = mid2 - 1

                return False
            
            elif matrix[mid1][0] < target:
                low1 = mid1 + 1

            else:
                high1 = mid1 - 1
            
        return False
        
        

        