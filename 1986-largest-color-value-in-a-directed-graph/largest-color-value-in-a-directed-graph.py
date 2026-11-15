from collections import deque
class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n=len(colors)
        q=deque()
        indeg=[0] *n
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            indeg[v]+=1
        for p in range(len(indeg)):
            if indeg[p]==0:
                q.append(p)
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            idx = ord(colors[i]) - ord('a')   
            dp[i][idx]=1
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for neigh in adj[node]:
                for c in range(26):
                    dp[neigh][c] = max(
                    dp[neigh][c],
                    dp[node][c] + (1 if c == ord(colors[neigh]) - ord('a') else 0))
                indeg[neigh]-=1
                if indeg[neigh]==0:
                    q.append(neigh)
               
        if len(ans)!=n:
            return -1
        return max(max(row) for row in dp)

