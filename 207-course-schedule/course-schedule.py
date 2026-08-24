class Solution:
    def canFinish(self, n: int, pr: List[List[int]]) -> bool:
        adj=[[] for _ in range(n)]
        visited=[False]*n
        for i in range(len(pr)):
            s=pr[i][0]
            d=pr[i][1]
            adj[d].append(s)
           
        path=[False] * n
        def mi(node):
            
            if path[node]:
                return False
            if visited[node]:
                return True

            path[node]=True
            visited[node]=True
            for i in range(len(adj[node])):
                neigh=adj[node][i]
                
                if mi(neigh)==False:
                    return False
            path[node]=False
            return True
        for i in range(n):
            if path[i]==False:
                if mi(i)==False:
                    return False
        return True
