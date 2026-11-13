class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n=len(vals)
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dict1={}
        for i in range(len(vals)):
            if vals[i] not in dict1:
                dict1[vals[i]]=[]
            dict1[vals[i]].append(i)
        rank=[0]*n
        parent=[]
        for u in range(n):
            parent.append(u)
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
        activate=[False]*n
        ans=n
        for values in sorted(dict1):
            for node in dict1[values]:
                activate[node]=True
            for node in dict1[values]:
                for neigh in adj[node]:
                    if activate[neigh]==True:
                        union(node,neigh)
            count = [0] * n
            roots = []

            for node in dict1[values]:
                root = find(node, parent)

                if count[root] == 0:
                    roots.append(root)

                count[root] += 1

            for root in roots:
                c = count[root]
                ans += c * (c - 1) // 2
        return ans
        

        
           