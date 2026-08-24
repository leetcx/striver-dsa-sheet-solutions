class Solution:
    def findCircleNum(self, edges: List[List[int]]) -> int:
        n=len(edges)
        adj =[[] for _ in range(n)]
        visited=[False] * n
        adj = [[] for _ in range(n)]
        p=0

        for i in range(n):
            for j in range(n):
                if edges[i][j] == 1 and i != j:
                    adj[i].append(j)
        def dfs(node):
            
           
            visited[node]= True
            for t in range(len(adj[node])):
                neigh=adj[node][t]
                if visited[neigh]==False:
                    dfs(neigh)
        for k in range(n):
            if visited[k]==False:
                dfs(k)
                p+=1
        return p
        
        





























