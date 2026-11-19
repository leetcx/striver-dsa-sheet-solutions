class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        INF = (1 << 30)-1
        cost=[INF] * n
        parent=[]
        for i in range(n):
            parent.append(i)
        rank=[0] * n
        def find(x,parent):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x],parent)
            return parent[x]
        def union(x,y,rank,parent,w):
            parent_x=find(x,parent)
            parent_y=find(y,parent)   
            if parent_x==parent_y:
                cost[parent_x]&=w
                return
            newcost=cost[parent_x] & cost[parent_y] & w
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
                cost[parent_x]=newcost

            elif rank[parent_x]<rank[parent_y]:
                parent[parent_x]=parent_y
                cost[parent_y]=newcost
            else:
                parent[parent_y]=parent_x
                rank[parent_x]+=1
                cost[parent_x]=newcost
        for u,v,w in edges:
            union(u,v,rank,parent,w)
        ans=[]
        for u,v in query:
            a=find(u,parent)
            b=find(v,parent)
            if a!=b:
                ans.append(-1)
            else:
                ans.append(cost[a])
        return ans
        
