class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = max(max(edge) for edge in edges)
        adj=[[] for _ in range(n+1)]
         
        c=  0
        for i in range(len(edges)):
            s=edges[i][0]
            d=edges[i][1]
            adj[s].append(d)
            adj[d].append(s)
        for j in range(len(adj)):
            if len(adj[j])==(n-1):
                c=j
        return c