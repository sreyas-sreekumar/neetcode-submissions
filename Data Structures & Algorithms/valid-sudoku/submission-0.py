class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for rowIndex in range(0,9):
            hashRow = set()
            for i in range(0,9):
                if board[rowIndex][i] == ".":
                    continue
                if board[rowIndex][i] in hashRow:
                    return False
                if board[rowIndex][i] not in hashRow:
                    hashRow.add(board[rowIndex][i])

        for colIndex in range(0,9):
            hashCol = set()
            for i in range (0,9):
                if board[i][colIndex] == ".":
                    continue
                if board[i][colIndex] in hashCol:
                    return False
                if board[i][colIndex] not in hashCol:
                    hashCol.add(board[i][colIndex])


        for row in range(0,9,3):
            for col in range (0,9,3):
                hashSquare = set()
                for i in range(0+row,3+row):
                    for j in range(0+col,3+col):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] not in hashSquare:
                            hashSquare.add(board[i][j])
                        else : 
                            return False
        return True
                