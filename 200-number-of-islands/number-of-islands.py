class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        m=len(grid)
        n=len(grid[0])
        visited=[[False] *n for _ in range(m)]
        p=0
        def valid(r,c,m,n):
            if r<0 or r>=m or c<0 or c>= n:
                return False
            return True
        def dfs(row,col,visited,grid):
            visited[row][col]=True
            for k in range(4):
                r=row+x[k]
                c=col+y[k]
                if valid(r,c,m,n) and visited[r][c]==False and grid[r][c]=='1':
                    dfs(r,c,visited,grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==False:
                    dfs(i,j,visited,grid)
                    p+=1
        return p
