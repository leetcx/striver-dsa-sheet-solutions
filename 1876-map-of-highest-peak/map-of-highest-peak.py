class Solution:
    def highestPeak(self, isw: list[list[int]]) -> list[list[int]]:
        m=len(isw)
        n=len(isw[0])
        q=deque()
        visited=[[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isw[i][j]==1:
                    q.append((i,j))
                    visited[i][j]=True
                    isw[i][j] = 0
        
        
        while q:
            p=len(q)
            while p:
                i,j=q.popleft()
                if i+1<m and visited[i+1][j]==False:
                    visited[i+1][j]=True
                    isw[i+1][j]=isw[i][j]+1
                    q.append((i+1,j))
                if i-1>=0 and visited[i-1][j]==False:
                    visited[i-1][j]=True
                    isw[i-1][j]=isw[i][j]+1
                    q.append((i-1,j))
                if j+1<n and visited[i][j+1]==False:
                    visited[i][j+1]=True
                    isw[i][j+1]=isw[i][j]+1
                    q.append((i,j+1))
                if j-1>=0 and visited[i][j-1]==False:
                    visited[i][j-1]=True
                    isw[i][j-1]=isw[i][j]+1
                    q.append((i,j-1))
                p-=1
        return isw
        
                

