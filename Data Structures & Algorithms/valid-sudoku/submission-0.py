class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for a in range(9):
            for b in range(9):
                if board[a][b] == ".":
                    continue
                if (board[a][b] in row[a] or 
                board[a][b] in column[b] or
                board[a][b] in box[(a//3, b//3)]):
                    return False
                row[a].add(board[a][b])
                column[b].add(board[a][b])
                box[(a//3, b//3)].add(board[a][b])
        return True