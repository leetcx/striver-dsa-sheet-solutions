
from collections import deque

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:

        # Step 1: Item graph
        adj = [[] for _ in range(n)]
        indeg = [0] * n

        for i in range(n):
            for j in beforeItems[i]:
                adj[j].append(i)
                indeg[i] += 1

        q = deque()

        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        itemorder = []

        while q:
            node = q.popleft()
            itemorder.append(node)

            for neigh in adj[node]:
                indeg[neigh] -= 1

                if indeg[neigh] == 0:
                    q.append(neigh)

        if len(itemorder) != n:
            return []

        # Step 2: Assign unique groups to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Step 3: Group graph
        newadj = [[] for _ in range(m)]
        newindeg = [0] * m

        for i in range(n):
            for j in beforeItems[i]:
                if group[i] != group[j]:
                    newadj[group[j]].append(group[i])
                    newindeg[group[i]] += 1

        q = deque()

        for i in range(m):
            if newindeg[i] == 0:
                q.append(i)

        grouporder = []

        while q:
            node = q.popleft()
            grouporder.append(node)

            for neigh in newadj[node]:
                newindeg[neigh] -= 1

                if newindeg[neigh] == 0:
                    q.append(neigh)

        if len(grouporder) != m:
            return []

        # Step 4: Put items into their respective groups
        finalans = [[] for _ in range(m)]

        for p in itemorder:
            z = group[p]
            finalans[z].append(p)

        # Step 5: Construct final answer using group order
        ans = []

        for g in grouporder:
            ans.extend(finalans[g])

        return ans
