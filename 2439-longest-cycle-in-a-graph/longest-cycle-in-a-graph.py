
class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        visited = [False] * n
        count = [1] * n
        inrecur = [False] * n

        def dfs(node, edges, path):
            if node == -1:
                return -1

            visited[node] = True
            inrecur[node] = True
            path.append(node)

            neigh = edges[node]

            if neigh != -1 and visited[neigh] and inrecur[neigh]:
                return count[node] - count[neigh] + 1

            elif neigh != -1 and not visited[neigh]:
                count[neigh] = count[node] + 1
                return dfs(neigh, edges, path)

            return -1

        result = -1

        for i in range(n):
            if not visited[i]:
                path = []
                result = max(result, dfs(i, edges, path))

                for node in path:
                    inrecur[node] = False

        return result
