class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        p=len(isConnected)
        adj=[[] for _ in range(p)]
        visited=[False] * (p)
        for i in range(len(isConnected)):
            for j in range(p):
                if i != j and isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        def dfs(adj,node):
            visited[node]=True
            for neigh in adj[node]:
                if visited[neigh]==False:
                    dfs(adj,neigh)
        count=0
        for i in range(len(adj)):
            if visited[i]==False:
                dfs(adj,i)
                count+=1
        return count
