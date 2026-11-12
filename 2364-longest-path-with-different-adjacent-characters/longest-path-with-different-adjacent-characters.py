class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        n = len(parent)

        adj = [[] for _ in range(n)]

        for i in range(1, n):
            p = parent[i]
            adj[p].append(i)

        count = [0] * n
        result = []

        def dfs(node):
            count[node] = 1

            for neigh in adj[node]:
                dfs(neigh)

                if s[node] != s[neigh]:
                    count[node] = max(count[node],
                                      1 + count[neigh])

            branches = []

            for neigh in adj[node]:
                if s[node] != s[neigh]:
                    branches.append(count[neigh])

            branches.sort(reverse=True)

            if len(branches) >= 2:
                result.append(1 + branches[0] + branches[1])
            elif len(branches) == 1:
                result.append(1 + branches[0])
            else:
                result.append(1)

        dfs(0)

        return max(result)