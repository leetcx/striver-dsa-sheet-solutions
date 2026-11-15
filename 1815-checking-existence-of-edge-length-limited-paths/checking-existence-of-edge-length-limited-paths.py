class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        parent=[]
        for i in range(n):
            parent.append(i)
        rank=[0]*n
        edgeList.sort(key=lambda x: x[2])
        for p in range(len(queries)):
            queries[p].append(p)
        queries.sort(key=lambda x:x[2])
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
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
            elif rank[parent_x]<rank[parent_y]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1
        c=0
        ans=[False] * len(queries)
        for u,v,limit,invalid in queries:
            for j in range(c,len(edgeList)):
                if limit>edgeList[j][2]:
                    c+=1
                    union(edgeList[j][0],edgeList[j][1])
                else:
                    break
            z=find(u,parent)
            m=find(v,parent)
            if z==m:
                ans[invalid]=True
        return ans

                
        