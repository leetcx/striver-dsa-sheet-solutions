from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        adj = [[] for _ in range(n)]
        for i in range(len(favorite)):
            adj[favorite[i]].append(i)
        visited = [False] * n
        count = 0
        longestcycle = 0
        happycouple = 0

        def bfs(node, adj, blocked):
            q = deque()
            q.append(node)
            visited = [False] * n
            visited[node] = True
            level = 0
            while q:
                p = len(q)
                while p > 0:
                    node = q.popleft()
                    for neigh in adj[node]:
                        if neigh != blocked and visited[neigh] == False:
                            visited[neigh] = True
                            q.append(neigh)
                    p -= 1
                level += 1
            return level - 1

        for i in range(len(favorite)):
            currnode = i
            currcount = 0
            mp = {}
            while not visited[currnode]:
                visited[currnode] = True
                mp[currnode] = currcount
                currcount += 1
                nextnode = favorite[currnode]
                if nextnode in mp:
                    cyclelength = currcount - mp[nextnode]
                    longestcycle = max(longestcycle, cyclelength)
                    if cyclelength == 2:
                        happycouple += (
                            2
                            + bfs(nextnode, adj, currnode)
                            + bfs(currnode, adj, nextnode)
                        )
                currnode = nextnode
        return max(happycouple, longestcycle)
