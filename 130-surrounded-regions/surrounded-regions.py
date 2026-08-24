class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        m=len(board)
        n=len(board[0])
        visited=[[False]*n for _ in range(m)]
        def valid(r,c,m,n):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            return True

        def dfs(row,col,board):
            for k in range(4):
                r=row+x[k]
                c=col+y[k]
                if valid(r,c,m,n) and board[r][c]=='O' and visited[r][c]==False:
                    visited[r][c]=True
                    dfs(r,c,board)

        for i in range(n):
            if board[0][i]=='O':
                visited[0][i]=True
                dfs(0,i,board)
        for j in range(n):
            if board[m-1][j]=='O':
                visited[m-1][j]=True
                dfs(m-1,j,board)
        for i in range(m):
            if board[i][0]=='O':
                visited[i][0]=True
                dfs(i,0,board)
        for j in range(m):
            if board[j][n-1]=='O':
                visited[j][n-1]=True
                dfs(j,n-1,board)
        for l in range(m):
            for t in range(n):
                if board[l][t]=='O' and visited[l][t]==False:
                    board[l][t]='X'
        
