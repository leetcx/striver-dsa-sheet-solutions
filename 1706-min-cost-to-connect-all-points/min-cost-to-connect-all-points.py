class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        adj=[]
        parent=[]
        rank=[0] * (len(points))
        for i in range(len(points)):
            parent.append(i)
        for i in range(len(points)):
            for j in range(len(points)):
                if i==j:
                    continue
                dist=abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
                adj.append((i,j,dist))
                
        adj.sort(key=lambda x:x[2])
        sum1=0
        def find(i,parent):
            if parent[i]==i:
                return i
            parent[i]=find(parent[i],parent)
            return parent[i]
        def union(i,j,parent,rank):
            parent_i=find(i,parent)
            parent_j=find(j,parent)
            if parent_i == parent[j]:
                return 
            if rank[parent_u]>rank[parent_v]:
                parent[parent_v]=parent_u
            elif rank[parent_u]<rank[parent_v]:
                parent[parent_u]=parent_v
            else:
                parent[parent_u]=parent_v
                rank[parent_v]+=1
        for u,v,w in adj:
            parent_u=find(u,parent)
            parent_v=find(v,parent)
            if parent_u != parent_v:
                sum1+=w
                union(u,v,parent,rank)
        return sum1

        