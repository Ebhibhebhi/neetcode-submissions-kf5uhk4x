class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        
        visit = set()
        q = deque()
        
        def addRoom(r, c):
            if (r == ROW or c == COL or
                r == -1 or c == -1 or
                (r,c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r,c))
            q.append([r,c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            distance+=1

