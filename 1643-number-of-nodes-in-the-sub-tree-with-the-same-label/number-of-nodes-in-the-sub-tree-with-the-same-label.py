class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count=[0] * 26
        result=[0] * n
        def dfs(node,adj,parent):
            nonlocal result
            nonlocal count
            beforevisiting = count[ord(labels[node]) - ord('a')]
            count[ord(labels[node]) - ord('a')]+=1
            for neigh in adj[node]:
                if neigh==parent:
                    continue
                dfs(neigh,adj,node)
            aftervisiting=count[ord(labels[node]) - ord('a')]
            result[node]=aftervisiting-beforevisiting
        dfs(0,adj,-1)
        return result