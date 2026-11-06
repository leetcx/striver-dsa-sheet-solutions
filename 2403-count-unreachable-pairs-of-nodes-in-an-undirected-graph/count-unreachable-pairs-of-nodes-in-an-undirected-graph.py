class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        
        parent=[]
        for i in range(n):
            parent.append(i)
        rank=[1]*n
        def find(i,parent):
            if parent[i]==i:
                return i
            parent[i]=find(parent[i],parent)
            return parent[i]
        def union(u,v,rank,parent):
            parent_u=find(u,parent)

            parent_v=find(v,parent)
            if parent_u==parent_v:
                return 
            if rank[parent_u]>rank[parent_v]:
                parent[parent_v]=parent_u
            elif rank[parent_u]<rank[parent_v]:
                parent[parent_u]=parent_v
            else:
                parent[parent_u]=parent_v
                rank[parent_v]+=1


        for i in range(len(edges)):
            union(edges[i][0],edges[i][1],rank,parent)
        dict1={}
        for i in range(n):
            root = find(i, parent)
            if root in dict1:
                dict1[root] += 1
            else:
                dict1[root] = 1
        score=0
        remaining=n
        for i in dict1:
            score += dict1[i] * (remaining - dict1[i])
            remaining -= dict1[i]
        return score

