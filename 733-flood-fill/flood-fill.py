class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        visited=[[False]*n for _ in range(m)]
        def valid(r,c,m,n):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            return True
        def dfs(row,col,color,visited,image):
            visited[row][col]=True
            for k in range(4):
                r=row+x[k]
                c=col+y[k]
                if valid(r,c,m,n) and visited[r][c]==False and image[r][c] !=color and image[r][c]==p:
                    image[r][c]=color
                    dfs(r,c,color,visited,image)
        if image[sr][sc] !=color:
            p=image[sr][sc]
            image[sr][sc]=color
            dfs(sr,sc,color,visited,image)
        return image