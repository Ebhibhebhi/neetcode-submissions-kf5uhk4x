class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0

        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r, c):
            nonlocal curr
            if (r == -1 or r == ROW or
                c == -1 or c == COL or
                grid[r][c] == 0):
                return
            grid[r][c] = 0
            curr+=1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    curr = 0
                    dfs(r, c)
                    area = max(area, curr)

        return area