class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        n=len(board)
        m=len(board[0])
        def dfs(board,m,n,i,j,x,y):
            board[i][j]='#'
            for k in range(4):
                row=i+x[k]
                col=j+y[k]
                if valid(row,col,m,n) and board[row][col] == 'O':
                    dfs(board,m,n,row,col,x,y)
        def valid(i,j,m,n):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True
        for j in range(m):
            if board[0][j]=='O':
                dfs(board,m,n,0,j,x,y)
        for j in range(m):
            if board[n-1][j]=='O':
                dfs(board,m,n,n-1,j,x,y)
        for i in range(n):
            if board[i][0]=='O':
                dfs(board,m,n,i,0,x,y)
        for i in range(n):
            if board[i][m-1]=='O':
                dfs(board,m,n,i,m-1,x,y)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='#':
                    board[i][j]='O'
                else:
                    board[i][j]='X'


