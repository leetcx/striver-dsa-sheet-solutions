class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def isbipartite(node):
            color=[-1]*(n+1)
            color[node]=1
            q=deque()
            q.append(node)
            component=[]
            while q:
                node=q.popleft()
                visited[node]=True
                component.append(node)
                for neigh in adj[node]:
                    if color[neigh]==-1:
                        color[neigh]=1-color[node]
                        q.append(neigh)
                        
                    elif color[neigh]==color[node]:
                        return False,[]
            return True,component
        def bfs(node):
            q=deque()
            q.append(node)
            visi=[False]*(n+1)
            visi[node]=True
            level=0
            while q:
                z=len(q)
                while z>0:
                    zode=q.popleft()
                    for neigh in adj[zode]:
                        if visi[neigh]==False:
                            visi[neigh]=True
                            q.append(neigh)
                    z-=1
                level+=1
            return level

        visited=[False]*(n+1)
        ans=0
        for i in range(1,n+1):
            if visited[i]==False:
                valid,component=isbipartite(i)
                if valid==False:
                    return -1
                maxi=0
                for node in component:
                    maxi=max(maxi,bfs(node))
                ans+=maxi
        return ans