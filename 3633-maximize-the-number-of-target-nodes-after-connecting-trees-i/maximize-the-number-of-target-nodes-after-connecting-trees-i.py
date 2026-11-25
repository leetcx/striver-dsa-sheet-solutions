class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        n=len(edges1)+1
        ans=[]
        if k==0:
            for i in range(n):
                ans.append(1)
            return ans 
        m=len(edges2)+1
        adj1=[[] for _ in range(n)]
        adj2=[[] for _ in range(m)]
        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[v].append(u)
            adj2[u].append(v)
        def bfs(node,limit,adj,range):
            count=1
            q=deque()
            visited=[False] * range
            q.append(node)
            visited[node]=True
            while q and limit>0:
                z=len(q)
                while z>0:
                    nody=q.popleft()
                    for neigh in adj[nody]:
                        if visited[neigh]==False:
                            count+=1
                            visited[neigh]=True
                            q.append(neigh)
                    z-=1
                limit-=1
            return count
        result=[0] * n
        for i in range(n):
            result[i]=bfs(i,k,adj1,n)
        dodge=float('-inf')
        for j in range(m):
            dodge=max(dodge,bfs(j,k-1,adj2,m))
        for i in range(n):
            result[i]+=dodge
        return result



