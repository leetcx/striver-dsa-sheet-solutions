
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:

        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda x: x[2])

        def kruskal(edges, forced=None):
            rank = [0] * n
            parent = [i for i in range(n)]

            def find(x):
                if parent[x] == x:
                    return x
                parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                parent_x = find(x)
                parent_y = find(y)

                if parent_x == parent_y:
                    return False

                if rank[parent_x] > rank[parent_y]:
                    parent[parent_y] = parent_x
                elif rank[parent_x] < rank[parent_y]:
                    parent[parent_x] = parent_y
                else:
                    parent[parent_x] = parent_y
                    rank[parent_y] += 1

                return True

            ans = 0
            count = 0

            if forced is not None:
                u, v, w, index = forced
                union(u, v)
                ans += w
                count += 1

            for u, v, w, index in edges:
                if forced is not None and index == forced[3]:
                    continue

                if union(u, v):
                    ans += w
                    count += 1

                if count == n - 1:
                    break

            return ans if count == n - 1 else float('inf')

        original = [edge[:] for edge in edges]

        original_mst = kruskal(original)

        arr = [[], []]

        for u, v, w, index in original:

            edges = [edge[:] for edge in original]
            edges = [edge for edge in edges if edge[3] != index]

            newmst = kruskal(edges)

            if newmst > original_mst:
                arr[0].append(index)

            else:
                forced_mst = kruskal(original, [u, v, w, index])

                if forced_mst == original_mst:
                    arr[1].append(index)

        return arr
