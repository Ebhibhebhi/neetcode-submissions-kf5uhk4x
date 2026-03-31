class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROW or c == COL or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0

            up = dfs(r+1,c)
            dw = dfs(r-1,c)
            le = dfs(r,c+1)
            ri = dfs(r,c-1)

            return 1 + up + dw + le + ri
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        
        return area