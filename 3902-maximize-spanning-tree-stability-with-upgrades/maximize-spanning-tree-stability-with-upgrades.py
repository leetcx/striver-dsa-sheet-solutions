class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def check(mid, k, edges):
            parent = list(range(n))
            rank = [0] * n

            def find(x):
                if x == parent[x]:
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
                elif rank[parent_y] > rank[parent_x]:
                    parent[parent_x] = parent_y
                else:
                    parent[parent_x] = parent_y
                    rank[parent_y] += 1

                return True

            upgrade = []

            # Mandatory edges
            for u, v, wt, m in edges:
                if m == 1:
                    if wt < mid:
                        return False

                    if not union(u, v):
                        return False

            # Normal edges and upgrade candidates
            for u, v, wt, m in edges:
                if m == 0:
                    if wt >= mid:
                        union(u, v)

                    elif wt * 2 >= mid:
                        upgrade.append((u, v))

            # Upgrade edges only when needed
            for u, v in upgrade:
                if find(u) != find(v):
                    if k <= 0:
                        return False

                    union(u, v)
                    k -= 1

            # Check connectivity
            root = find(0)

            for i in range(1, n):
                if find(i) != root:
                    return False

            return True

        l = 1
        r = 2 * (10**5)
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if check(mid, k, edges):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans