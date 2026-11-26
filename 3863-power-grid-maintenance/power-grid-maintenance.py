
from sortedcontainers import SortedList
from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        parent = [i for i in range(c+1)]
        rank = [0] * (c+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return

            if rank[pu] < rank[pv]:
                parent[pu] = pv
            elif rank[pu] > rank[pv]:
                parent[pv] = pu
            else:
                parent[pv] = pu
                rank[pu] += 1

        # Build connected components
        for u, v in connections:
            union(u, v)

        # Store online nodes in each component
        set1 = {}

        for i in range(1, c+1):
            key = find(i)

            if key not in set1:
                set1[key] = SortedList()

            set1[key].add(i)

        ans = []

        for u, v in queries:
            key = find(v)

            if u == 1:
                if v in set1[key]:
                    ans.append(v)
                elif set1[key]:
                    ans.append(set1[key][0])
                else:
                    ans.append(-1)

            else:
                set1[key].discard(v)

        return ans
