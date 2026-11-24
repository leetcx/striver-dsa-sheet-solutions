class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent=[]
        rank=[0] *n
        for i in range(n):
            parent.append(i)
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
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
            elif rank[parent_y]>rank[parent_x]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1
        for u,v in edges:
            union(u,v)
        
        nodes={}
        for i in range(n):
            p=find(i)
            if p not in nodes:
                nodes[p]=1
            else:
                nodes[p]+=1
        edgecount={}
        for u,v in edges:
            root=find(u)
            if root not in edgecount:
                edgecount[root]=1
            else:
                edgecount[root]+=1
        count=0
        for root in nodes:
            k=nodes[root]
            if  root in edgecount:
                if edgecount[root]==k*(k-1)//2:
                    count+=1
            else:
                count+=1
        return count
        
            
        