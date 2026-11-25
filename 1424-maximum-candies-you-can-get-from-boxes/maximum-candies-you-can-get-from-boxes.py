from collections import deque

class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        n = len(status)
        q = deque()

        haskey = [False] * n
        visited = [False] * n
        waiting = [False] * n

        for i in initialBoxes:
            if status[i] == 1:
                q.append(i)
                visited[i] = True
            else:
                waiting[i] = True

        sum1 = 0

        while q:
            node = q.popleft()
            sum1 += candies[node]

            for key in keys[node]:
                haskey[key] = True

                if waiting[key] and not visited[key]:
                    q.append(key)
                    waiting[key] = False
                    visited[key] = True

            for neigh in containedBoxes[node]:
                if visited[neigh]:
                    continue

                if status[neigh] == 1 or haskey[neigh]:
                    q.append(neigh)
                    visited[neigh] = True
                else:
                    waiting[neigh] = True

        return sum1