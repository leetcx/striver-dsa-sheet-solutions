class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(mid,k,edges):
            parent=[]
            for i in range(n):
                parent.append(i)
            rank=[0] * n
            def find(x):
                if x==parent[x]:
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
            for u,v,w,m in edges:
                if m==1:
                    parent_u=find(u)
                    parent_v=find(v)
                    if parent_u==parent_v:
                        return False
                    union(u,v)
        
            upgrade=[]
            for u,v,wt,m in edges:
                if m==1:
                    if wt<mid:
                        return False
                    union(u,v)
                else:
                    if wt>=mid:
                        union(u,v)
                    elif wt*2>=mid:
                        upgrade.append((u,v))
            for u,v in upgrade:
                parent_u=find(u)
                parent_v=find(v)
                if parent_u!=parent_v:
                    if k<=0:
                        return False
                    union(u,v)
                    k-=1
            for i in range(n):
                find(i)

            return len(set(parent)) == 1

       


        l=1
        r=2*(10**5)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if check(mid,k,edges):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans