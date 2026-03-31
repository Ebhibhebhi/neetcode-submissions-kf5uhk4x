class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        not_surrounded = set()
        def dfs(r, c):
            nonlocal visited, surrounded
            if not surrounded:
                return
            if board[r][c] == "X" or (r,c) in visited:
                return
            if (r == 0 or c == 0 or
                r == ROW - 1 or c == COL - 1):
                surrounded = False
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O" and (r,c) not in not_surrounded:
                    visited = set()
                    surrounded = True
                    dfs(r, c)
                    if surrounded:
                        for el in visited:
                            i, j = el
                            board[i][j] = "X"
                    else:
                        for el in visited:
                            not_surrounded.add(el)
        