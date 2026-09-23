class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board=[["."]*n for _ in range(n)]
        ans=[]
        cols={}
        diag1={}
        diag2={}
        def isvalid(board,row,i,diag1,diag):
            return (i not in cols )and (row+i not in diag1) and (row-i not in diag2)
            
        def solve(board,row):
            
            nonlocal ans
            if row>=n:
                ans.append(["".join(r) for r in board])
                return
            for i in range(n):
                if isvalid(board,row,i,diag1,diag2):
                    board[row][i]="Q"
                    cols[i]=True
                    diag1[row+i]=True
                    diag2[row-i]=True
                    solve(board,row+1)
                    board[row][i]="."
                    del cols[i]
                    del diag1[row+i]
                    del diag2[row-i]
        solve(board,0)
        return ans
                    
