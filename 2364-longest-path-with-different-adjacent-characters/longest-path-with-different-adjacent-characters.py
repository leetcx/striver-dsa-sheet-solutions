
class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        n = len(parent)

        adj = [[] for _ in range(n)]

        for node in range(1, n):
            p = parent[node]
            adj[p].append(node)
            adj[node].append(p)

        result = 1

        def dfs(node, parent, adj):
            nonlocal result

            longest = 0
            secondlargest = 0

            for neigh in adj[node]:
                if neigh == parent:
                    continue

                childlength = dfs(neigh, node, adj)

                if s[neigh] == s[node]:
                    continue

                if childlength > secondlargest:
                    secondlargest = childlength

                if secondlargest > longest:
                    temp = longest
                    longest = secondlargest
                    secondlargest = temp

            p = 1 + max(longest, secondlargest)
            d = 1
            z = 1 + longest + secondlargest

            result = max(result, p, d, z)

            return max(p, d)

        dfs(0, -1, adj)
        return result
