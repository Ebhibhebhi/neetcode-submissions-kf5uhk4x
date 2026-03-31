class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0],(0,0)]]

        def addnei(distance, r, c):
            if (r == N or c == N
                or r < 0 or c < 0
                or (r,c) in visit):
                return

            distance = max(distance, grid[r][c])
            heapq.heappush(minH,[distance, (r,c)])
        
        res = float("inf")

        while minH:
            distance, node = heapq.heappop(minH)

            if node == (N-1, N-1):
                distance = max(distance, grid[N-1][N-1])
                res = distance
                break

            visit.add(node)

            r, c = node

            addnei(distance, r+1,c)
            addnei(distance, r-1,c)
            addnei(distance, r,c+1)
            addnei(distance, r,c-1)
        
        return res
            



            