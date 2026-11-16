class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n=len(bombs)
        adj=[[] for _ in range(n)]
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i==j:
                    continue
                xi=bombs[i][0]
                xj=bombs[j][0]
                yi=bombs[i][1]
                yj=bombs[j][1]
                ri=bombs[i][2]
                dist=((xi-xj)**2) + ((yi-yj)**2)
                if dist<=(ri**2):
                    adj[i].append(j)
        def dfs(node,adj,visited):
            count=1
            visited[node]=True
            for neigh in adj[node]:
                if visited[neigh]==False:
                    
                    count+=dfs(neigh,adj,visited)
            return count
        ans=1
        for i in range(n):
            visited=[False] * n
            
                
            ans=max(ans,dfs(i,adj,visited))
        return ans