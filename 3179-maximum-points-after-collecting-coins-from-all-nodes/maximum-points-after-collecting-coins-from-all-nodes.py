class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        p={}
        def dfs(i,parent,power,adj):
            if power>=14:
                return 0
            state=(i,power)
            if state in p:
                return p[state]
            case1=(coins[i]>>power)-k
            case2=(coins[i]>>power+1)
            for j in adj[i]:
                if j != parent:
                    case1+=dfs(j,i,power,adj)
                    case2+=dfs(j,i,power+1,adj)
            p[state]= max(case1,case2)
            return p[state]
        adj=[[] for _ in range(len(edges)+1)]
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        return dfs(0,-1,0,adj)