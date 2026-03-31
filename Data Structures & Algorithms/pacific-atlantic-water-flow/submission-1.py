class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, visited, past):
            if (r == -1 or c == -1 or
            r == ROW or c == COL or (r,c) in visited or
            heights[r][c] < past):
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW - 1, c, atlantic, heights[ROW-1][c])
        
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL - 1, atlantic, heights[r][COL-1])
        
        for el in pacific:
            if el in atlantic:
                r, c = el
                res.append([r,c])

        return res
