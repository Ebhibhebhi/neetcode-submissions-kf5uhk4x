class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        
        visit = set()
        q = deque()
        
        def addnei(r, c):
            if r == ROW or c == COL or r < 0 or c < 0 or (r, c) in visit or grid[r][c] == -1:
                return
            
            q.append([r, c])
            visit.add((r,c))
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        distance = 0

        while q:

            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
    
                addnei(r+1,c)
                addnei(r-1,c)
                addnei(r,c+1)
                addnei(r,c-1)
            
            distance += 1
        
                    

                










            