class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[v].append(u)
        ans=[[] for _ in range(n)]
        def bfs(node):
            q=deque()
            q.append(node)
            visited=[False] * n
            visited[node]=True
            while q:
                nody=q.popleft()
                if nody!=node:
                    ans[node].append(nody)
                for neigh in adj[nody]:
                    if visited[neigh]==False:
                        visited[neigh]=True
                        q.append(neigh)
        for i in range(n):
            bfs(i)
            ans[i].sort()
        return ans
                

        