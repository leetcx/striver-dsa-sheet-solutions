class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board=[["."]*n for _ in range(n)]
        ans=[]
        def isvalid(board,row,i):
            for p in range(row,-1,-1):
                if board[p][i]=="Q":
                    return False
                    break
            r,c=row,i
            while r>=0 and c<n:
                if board[r][c]=="Q":
                    return False
                    break
                r-=1
                c+=1
            r,c=row,i
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                    break
                r-=1
                c-=1
            return True
            
        def solve(board,row):
            
            nonlocal ans
            if row>=n:
                ans.append(["".join(r) for r in board])
                return
            for i in range(n):
                if isvalid(board,row,i):
                    board[row][i]="Q"
                    solve(board,row+1)
                    board[row][i]="."
        solve(board,0)
        return ans
                    
