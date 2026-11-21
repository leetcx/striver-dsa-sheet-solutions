class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n=len(stones)
        rank=[0]*n
        parent=[]
        for i in range(n):
            parent.append(i)
        def find(x,parent):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x],parent)
            return parent[x]
        def union(x,y):
            parent_x=find(x,parent)
            parent_y=find(y,parent)
            if parent_x == parent_y:
                return
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
            elif rank[parent_y]>rank[parent_x]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1

        count=0
        for i in range(len(stones)):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    if find(i,parent) !=find(j,parent):
                        union(i,j)
                        count+=1
        return count

            