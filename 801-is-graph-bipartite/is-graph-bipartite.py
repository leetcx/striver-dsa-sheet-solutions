class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1] * n
        visited=[False]*n

        def dfs(node,color,visited,c):
            visited[node]=True
            color[node]=c
            for i in range(len(graph[node])):
                neigh=graph[node][i]
                if  color[neigh]==c:
                    return False
                if visited[neigh]==False and color[neigh]!=c:
                    if dfs(neigh,color,visited,1-c)==False:
                        return False
            return True
        for i in range(n):
            if visited[i]==False:
                if dfs(i,color,visited,0)==False:
                    return False
        return True
