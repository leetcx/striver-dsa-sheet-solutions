class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        parent_alice=[]
        parent_bob=[]
        rankalice=[0]*(n+1)
        rankbob=[0]*(n+1)
        for i in range(n+1):
            parent_alice.append(i)
            parent_bob.append(i) 
        def find(x,parent):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x],parent)
            return parent[x]
        def union(x,y,parent,rank):
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

        count=0
        for type1,u,v in  edges:
            if type1==3:
                merged=False
                if find(u,parent_alice) != find(v,parent_alice):
                    union(u,v,parent_alice,rankalice)
                    merged=True
                if find(u, parent_bob) != find(v, parent_bob):
                    union(u, v, parent_bob,rankbob) 
                    merged=True
                if not merged:
                    count+=1
                 
        for type1,u,v in edges:
            if type1==2:
                if find(u, parent_bob) != find(v, parent_bob):
                    union(u, v, parent_bob,rankbob)
                else:
                    count+=1
        for type1,u,v in edges:
            if type1==1:
                if find(u,parent_alice) != find(v,parent_alice):
                    union(u,v,parent_alice,rankalice)
                else:
                    count+=1
        compo=1
        for i in range(2,n+1):
            if find(i,parent_alice) != find(1,parent_alice):
                return -1
            if find(i,parent_bob) != find(1,parent_bob):
                return -1
        return count

        
        

