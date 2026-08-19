class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        p=len(graph)
        colors=[-1] * p
        res=True
        def dfs(colors,node,c,graph):
            nonlocal res
            colors[node]=c
            for j in range(len(graph[node])):
                neigh=graph[node][j]
                if colors[neigh] !=-1 and colors[neigh]==c:
                    res=False
                if colors[neigh]== -1:
                    dfs(colors,neigh,(1-c),graph)

                    
        for i in range(p):
            if colors[i]==-1:
                dfs(colors,i,0,graph)
        return res