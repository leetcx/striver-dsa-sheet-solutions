from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        z=m*n
        parent=[]
        for i in range(z):
            parent.append(i)
        size=[0] * z
        for i in range(m):
            for j in range(n):
                index=(i*n+j)
                if grid[i][j]>0:
                    size[index]=grid[i][j]
        def find(x,parent):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x],parent)
            return parent[x]
        def union(x,y):
            parent_x=find(x,parent)
            parent_y=find(y,parent)
            if parent_x==parent_y:
                return
            if size[parent_x]>size[parent_y]:
                parent[parent_y]=parent_x
                size[parent_x]+=size[parent_y]
            elif size[parent_x]<size[parent_y]:
                parent[parent_x]=parent_y
                size[parent_y]+=size[parent_x]
            else:
                parent[parent_x]=parent_y
                size[parent_y]+=size[parent_x]
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    node=(i*n+j)
                    for p,k in direction:
                        nr=p+i
                        nc=j+k
                        if nr>=0 and nr<m and nc<n and nc>=0 and grid[nr][nc]>0:
                            
                            neighbour=nr*n+nc
                            union(node,neighbour)
        return max(size)

