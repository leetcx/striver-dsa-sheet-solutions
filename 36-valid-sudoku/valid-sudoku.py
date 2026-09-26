class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def check(board,row,col):
            count=0
            z=0
            for i in range(9):

                if board[row][i]==board[row][col]:
                    count+=1
                if count>1:
                    return False
                if board[i][col] == board[row][col]:
                    z+=1
                if z>1:
                    return False
            startrow=(row//3)*3
            endrow=(col//3)*3
            g=0
            for t in range(startrow,startrow+3):
                for mp in range(endrow,endrow+3):
                    if board[t][mp]==board[row][col]:
                        g+=1
                    if g>1:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if check(board,i,j)==False:
                    return False
        return True

                

