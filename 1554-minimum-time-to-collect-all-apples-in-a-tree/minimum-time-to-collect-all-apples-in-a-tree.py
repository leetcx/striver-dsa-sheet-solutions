
class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        visited = [False] * n
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dfscount = 0
        minstep = 0

        def dfs(node, adj):
            nonlocal dfscount, minstep

            found = hasApple[node]

            for neigh in adj[node]:
                if visited[neigh] == False:
                    visited[neigh] = True
                    

                    child_found = dfs(neigh, adj)

                    if child_found:
                        minstep += 1

                    
                    found = found or child_found

            return found

        visited[0] = True
        dfs(0, adj)

        return minstep * 2
