class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited = [[False] * m for _ in range(n)]
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        res=0
        
        
        def dfs(grid,i,j,visited,x,y,m,n):
            visited[i][j]=True
            for k in range(0,4):
                row=i+x[k]
                col=j+y[k]
                if valid(row,col,m,n) and grid[row][col]=='1' and visited[row][col]==False:
                    dfs(grid,row,col,visited,x,y,m,n)
        def valid(i,j,m,n):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True
        for i in range(n):
            for j in range(m):
                if grid[i][j]== '1' and visited[i][j]==False:
                    dfs(grid,i,j,visited,x,y,m,n)
                    res+=1
        return res


