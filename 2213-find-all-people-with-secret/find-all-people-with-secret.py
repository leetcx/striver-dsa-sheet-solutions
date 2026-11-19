
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:

        meetings.sort(key=lambda x: x[2])

        ans = {0, firstPerson}
        i = 0

        while i < len(meetings):
            time = meetings[i][2]
            adj = defaultdict(list)
            
            # Build graph for the current timestamp
            while i < len(meetings) and meetings[i][2] == time:
                u, v, t = meetings[i]
                adj[u].append(v)
                adj[v].append(u)
                i += 1

            q = deque()
            visited = set()

            # Add people who already know the secret
            for person in adj:
                if person in ans:
                    q.append(person)
                    visited.add(person)

            # BFS
            while q:
                node = q.popleft()

                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        ans.add(nei)
                        q.append(nei)

        return list(ans)
