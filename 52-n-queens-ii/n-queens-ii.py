class Solution:
    def totalNQueens(self, n: int) -> int:
        board=[["."] * n for _ in range(n)]
        count=0
        def isvalid(board,row,col):
            for p in range(row - 1,-1,-1):
                if board[p][col] == "Q":
                    return False
            r=row
            c=col
            while r-1>=0 and c-1>=0:
                if board[r-1][c-1]=="Q":
                    return False
                r-=1
                c-=1
            r=row
            c=col
            while r-1>=0 and c+1<n:
                if board[r-1][c+1]=="Q":
                    return False
                r-=1
                c+=1
            return True

         
        def find(board,row):
            nonlocal count
            if row>=n:
                count+=1
                return


            for col in range(n):
                if isvalid(board,row,col):
                    board[row][col]="Q"
                    find(board,row+1)
                    board[row][col]="."
        find(board,0)
        return count
        
                
                
            
