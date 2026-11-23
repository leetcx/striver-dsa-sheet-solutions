class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        maxarea=float('-inf')
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        parent=[0] * (m*m)
        size=[0] * (m*m)
        for i in range(m):
            for j in range(m):
                index=i*m+j
                parent[index]=index
                size[index]=grid[i][j]
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent_x=find(x)
            parent_y=find(y)
            if parent_x==parent_y:
                return
            if size[parent_x]>size[parent_y]:
                parent[parent_y]=parent_x
                size[parent_x]+=size[parent_y]

            elif size[parent_y]>size[parent_x]:
                parent[parent_x]=parent_y
                size[parent_y]+=size[parent_x]
            else:
                parent[parent_x]=parent_y
                size[parent_y]+=size[parent_x]
        for i in range(m):
            for j in range(m):
                if grid[i][j]==1:
                    index=i*m+j
                    for p ,k in direction:
                        nr=i+p
                        nc=k+j
                        
                        if nr>=0 and nr<m and nc>=0 and nc<m:
                            nodyy=nr*m+nc
                            if grid[nr][nc]==1:
                                union(index,nodyy)
        ans=0
        for i in range(m):
            for j in range(m):
                if grid[i][j]==0:
                    total=1
                    set1=set()
                    for p,k in direction:
                        nr=p+i
                        nc=k+j
                        if nr>=0 and nr<m and nc>=0 and nc<m:
                            nora=nr*m+nc
                            if grid[nr][nc]==1:
                                parent_nody=find(nora)
                                if parent_nody not in set1:
                                    total+=size[parent_nody]
                                    set1.add(parent_nody)
                    ans=max(ans,total)
        if ans==0:
            return m*m
        return ans



                
        
