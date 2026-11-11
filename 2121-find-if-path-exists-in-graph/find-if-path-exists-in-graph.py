class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q=deque()
        q.append(source)
        visited=[False] * n
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for neigh in adj[node]:
                if visited[neigh]==False:
                    q.append(neigh)
                    visited[neigh]=True
        return False
