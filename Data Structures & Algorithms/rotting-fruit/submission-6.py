class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        fresh = 0
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1

        def addcell(r,c):
            nonlocal fresh
            if (r == ROW or c == COL or
                r < 0 or c < 0 or grid[r][c] == 0 or
                grid[r][c] == 2):
                return
            grid[r][c] = 2
            q.append((r,c))
            fresh -= 1
    
        t = 0
        last_fresh = -1

        while q and fresh > 0:

            for i in range(len(q)):

                r, c = q.popleft()

                last_fresh = fresh

                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)

            t += 1
            
        return t if fresh == 0 else -1

                





            
        
                    




        