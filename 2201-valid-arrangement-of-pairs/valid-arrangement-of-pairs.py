class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        from collections import defaultdict

        adj = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        for u, v in pairs:
            adj[u].append(v)
            indeg[v] += 1
            outdeg[u] += 1

        start = pairs[0][0]

        for i in outdeg:
            if outdeg[i] - indeg[i] == 1:
                start = i
                break

        ans = []
        st = [start]

        while st:
            if adj[st[-1]]:
                neigh = adj[st[-1]].pop()
                st.append(neigh)
            else:
                ans.append(st.pop())

        ans.reverse()

        result = []
        for i in range(len(ans) - 1):
            result.append([ans[i], ans[i + 1]])

        return result