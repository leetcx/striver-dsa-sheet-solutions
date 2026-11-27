class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return

            if rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
            elif rank[parent_v] > rank[parent_u]:
                parent[parent_u] = parent_v
            else:
                parent[parent_u] = parent_v
                rank[parent_v] += 1

        # Build DSU
        for u, v in allowedSwaps:
            union(u, v)

        # Store source frequencies in each component
        component = {}

        for i in range(n):
            p = find(i)

            if p not in component:
                component[p] = {}

            if source[i] not in component[p]:
                component[p][source[i]] = 1
            else:
                component[p][source[i]] += 1

        # Calculate minimum Hamming distance
        diff = 0

        for i in range(n):
            p = find(i)

            if target[i] in component[p] and component[p][target[i]] > 0:
                component[p][target[i]] -= 1
            else:
                diff += 1

        return diff
