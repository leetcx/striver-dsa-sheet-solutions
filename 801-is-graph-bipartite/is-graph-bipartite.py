class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        p=len(graph)
        color=[-1] *  p
        visited=[False] *p
        c=0
        def dfs(node,graph,color,c):
            visited[node]=True
            color[node]=c
            for t in range(len(graph[node])):
                neigh=graph[node][t]
                if visited[neigh]==True and color[neigh]==c:
                    return False
                if visited[neigh]==False:
                    if dfs(neigh,graph,color,1-c)==False:
                        return False
            return True
                    
        for i in range(p):
            if visited[i]==False:
                if dfs(i,graph,color,0)==False:
                    return False
        return True