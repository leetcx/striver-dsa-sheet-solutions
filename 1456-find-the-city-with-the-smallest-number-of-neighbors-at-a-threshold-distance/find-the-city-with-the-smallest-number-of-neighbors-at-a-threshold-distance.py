class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], hold: int) -> int:
        distance=[[float('inf')] * n for _ in range(n)]
        for u,v,w in edges:
            distance[u][v]=w
            distance[v][u]=w
        for i in range(n):
            distance[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
        skip=float('inf')
        ans=0
        for i in range(n):
            count=0
            for j in range(n):
                if i != j and distance[i][j]<=hold:
                    count+=1
            if count<=skip:
                ans=i
                skip=count
        return ans
