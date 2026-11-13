class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        groups = {}
        for i in range(n):
            if vals[i] not in groups:
                groups[vals[i]] = []
            groups[vals[i]].append(i)

        parent = list(range(n))
        isactive = [False] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu != pv:
                parent[pv] = pu

        ans = n

        for value in sorted(groups):
            nodes = groups[value]

            for node in nodes:
                isactive[node] = True

            for node in nodes:
                for neigh in adj[node]:
                    if isactive[neigh]:
                        union(node, neigh)

            roots = []

            for node in nodes:
                roots.append(find(node))

            roots.sort()

            j = 0
            sz = len(roots)

            while j < sz:
                count = 0
                curr_parent = roots[j]

                while j < sz and roots[j] == curr_parent:
                    count += 1
                    j += 1

                ans += count * (count - 1) // 2

        return ans