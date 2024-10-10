class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowNum = 9
        colNum = 9

        rows = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        cols = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        boxes = {(0,0): set(), (0,1): set(), (0,2): set(), (1,0): set(), (1,1): set(), (1,2): set(), (2,0): set(), (2,1): set(), (2,2): set()}

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] != ".":
                    # print(i, j)
                    if board[i][j] in rows[i+1]:
                        # print("row")
                        return False
                    else:
                        rows[i+1].add(board[i][j])

                    if board[i][j] in cols[j+1]:
                        # print(cols, i, j)
                        return False
                    else:
                        cols[j+1].add(board[i][j])

                    if board[i][j] in boxes[(i//3, j//3)]:
                        # print("box")
                        return False
                    else:
                        boxes[(i//3, j//3)].add(board[i][j])
                        # print(boxes)
        
        return True