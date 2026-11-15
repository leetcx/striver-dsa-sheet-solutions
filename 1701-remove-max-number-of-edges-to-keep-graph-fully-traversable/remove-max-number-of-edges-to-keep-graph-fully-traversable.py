class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        aliceparent=list(range(n + 1))
        bobparent=list(range(n + 1))
        alicerank = [0] * (n + 1)
        bobrank = [0] * (n + 1)
        def find(node,parent):
            if node==parent[node]:
                return node
            parent[node]=find(parent[node],parent)
            return parent[node]
        def union(x,y,rank,parent):
            parent_x=find(x,parent)
            parent_y=find(y,parent)
            if parent_x==parent_y:
                return False
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
            elif rank[parent_x]<rank[parent_y]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1
            return True
        count=0
        for type1,u,v in edges:
            if type1==3:
                a=union(u,v,alicerank,aliceparent)
                b=union(u,v,bobrank,bobparent)
                if a==False and b==False:
                    count+=1
        for type1,u,v in edges:
            if type1==1:
                a=union(u,v,alicerank,aliceparent)
                if a==False:
                    count+=1
        for type1,u,v in edges:
            if type1==2:
            
                b=union(u,v,bobrank,bobparent)
                if b==False:
                    count+=1
        aliceroot=find(1,aliceparent)
        bobroot=find(1,bobparent)
        for j in range(1,n+1):
            if find(j,aliceparent) != aliceroot:
                return -1
            if find(j,bobparent) != bobroot:
                return -1
        return count
