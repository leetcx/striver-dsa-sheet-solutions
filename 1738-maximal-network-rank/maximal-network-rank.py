class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                count=0
                p=len(adj[i])
                q=len(adj[j])
                if j in adj[i]:
                    count=1
                else:
                    count=0
                ans=max(ans,p+q-count)
        return ans
        
            
        
                
