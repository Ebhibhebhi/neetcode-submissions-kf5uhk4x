class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        num_fresh = 0
        visited = set()
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    num_fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        
        num_rotten = len(q)

        def spread(r, c):
            nonlocal num_fresh, num_rotten
            if (r == ROW or c == COL or r == -1 or c == -1 or
            grid[r][c] == 0 or grid[r][c] == 2 or
            (r,c) in visited):
                return
            
            visited.add((r,c))
            q.append([r,c])
            num_fresh -= 1
            num_rotten +=1

        time = 0

        while q:
            curr_fresh = num_fresh
            curr_rotten = num_rotten
            for i in range(len(q)):
                r, c = q.popleft()

                spread(r+1, c)
                spread(r-1, c)
                spread(r, c+1)
                spread(r, c-1)
            
            if num_fresh > 0 and curr_fresh == num_fresh:
                return -1
            
            if num_rotten == curr_rotten:
                return time
            
            time+=1
        
        return 0 if num_fresh == 0 else -1



        