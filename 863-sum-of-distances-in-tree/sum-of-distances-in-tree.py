class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = [0] * n
        ans = [0] * n
        root_result = [0]

        def dfsBase(curr_node, prev_node, curr_depth):

            total_count = 1

            root_result[0] += curr_depth

            for child in adj[curr_node]:

                if child == prev_node:
                    continue

                total_count += dfsBase(
                    child, curr_node, curr_depth + 1
                )

            count[curr_node] = total_count

            return total_count
        dfsBase(0, -1, 0)

        ans[0] = root_result[0]

        def dfs(curr_node, prev_node):

            for child in adj[curr_node]:

                if child == prev_node:
                    continue

                ans[child] = (
                    ans[curr_node] - count[child]
                    + (n - count[child])
                )

                dfs(child, curr_node)

        

        dfs(0, -1)

        return ans