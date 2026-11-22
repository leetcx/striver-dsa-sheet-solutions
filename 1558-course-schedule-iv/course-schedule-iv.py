from collections import deque

class Solution:
    def checkIfPrerequisite(self, n: int, pr: list[list[int]], queries: list[list[int]]) -> list[bool]:

        if pr==[]:
            return [False]*len(queries)

        indegree=[0]*n
        adj=[[] for _ in range(n)]

        for u,v in pr:
            indegree[v]+=1
            adj[u].append(v)

        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)

        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)

            for neigh in adj[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)

        if len(ans)!=n:
            return [False]*len(queries)

        pos={}
        for i,node in enumerate(ans):
            pos[node]=i

        def dfs(u,v,visited):
            if u==v:
                return True

            visited[u]=True

            for neigh in adj[u]:
                if not visited[neigh]:
                    if dfs(neigh,v,visited):
                        return True

            return False

        mainans=[]

        for u,v in queries:
            if pos[u]<pos[v]:
                visited=[False]*n
                mainans.append(dfs(u,v,visited))
            else:
                mainans.append(False)

        return mainans