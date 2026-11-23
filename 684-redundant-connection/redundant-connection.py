class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n=len(edges)
        parent=[]
        for i in range(n+1):
            parent.append(i)
        rank=[0]*(n+1)
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
            elif rank[parent_y]>rank[parent_x]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1
        
        for u,v in edges:
            parent_u=find(u,parent)
            parent_v=find(v,parent)
            if parent_u==parent_v:
                return [u,v]
            else:
                union(u,v)
        