class Solution:
    def possibleBipartition(self, p: int, graph: List[List[int]]) -> bool:
       
        color=[-1] *  (p+1)
        visited=[False] *(p+1)
        c=0
        adj=[[] for _ in range(p+1)]
        for i in range(len(graph)):
            s=graph[i][0]
            d=graph[i][1]
            adj[s].append(d)
            adj[d].append(s)
        def dfs(node,adj,color,c):
            visited[node]=True
            color[node]=c
            for t in range(len(adj[node])):
                neigh=adj[node][t]
                if visited[neigh]==True and color[neigh]==c:
                    return False
                if visited[neigh]==False:
                    if dfs(neigh,adj,color,1-c)==False:
                        return False
            return True
                    
        for i in range(p+1):
            if visited[i]==False:
                if dfs(i,adj,color,0)==False:
                    return False
        return True