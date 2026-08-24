class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        r=len(edges)        
       
        adj=[[] for _ in range(r+1)]
        def dfs(node,target,visited):
            if node==target:
                return True
            visited[node]=True
            for k in range(len(adj[node])):
                neigh=adj[node][k]
                if visited[neigh]==False:
                    if dfs(neigh,target,visited):
                        return True
            return False

        
        for i in range(len(edges)):
            visited=[False] *(r+1)
            p=edges[i][0]
            c=edges[i][1]
            
            if dfs(p,c,visited):
                return [p,c]
            adj[p].append(c)
            adj[c].append(p)
            