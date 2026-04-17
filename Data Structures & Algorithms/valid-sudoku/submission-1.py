class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for x in range(9):
                if board[i][x] == ".":
                    continue
                if board[i][x] in cols[x] or board[i][x] in rows[i] or board[i][x] in squares[(i//3,x//3)]:
                    return False
                cols[x].add(board[i][x])
                rows[i].add(board[i][x])
                squares[(i//3,x//3)].add(board[i][x])
        return True

                
                
        