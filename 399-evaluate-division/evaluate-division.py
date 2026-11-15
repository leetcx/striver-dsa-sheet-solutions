class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        known = set()

        for i in range(len(values)):
            u = equations[i][0]
            v = equations[i][1]

            wt = values[i]
            wt1 = 1 / values[i]
 
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []

            adj[u].append((v, wt))
            adj[v].append((u, wt1))

            known.add(u)
            known.add(v)
        ans=[]
        def dfs(node,target,visited,adj,prod):
            if node==target:
                return prod
            visited.add(node)
            for neigh in adj[node]:
                nody=neigh[0]
                w=neigh[1]
                if nody not in visited:
                    result=dfs(nody,target,visited,adj,prod*w)
                    if result!=-1.0:
                        return result
            return -1.0

                    
                    
            return -1.0
        for u,v in queries:
            if u not in known or v not in known:
                ans.append(-1.0)
                continue
            source= u
            dest= v
            visited=set()
            
            
            ans.append(dfs(source,dest,visited,adj,1.0))
        return ans
            
        

