class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount)

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

# Establish parent-child relationship
        parent = [-1] * n
        parent[0] = 0

        def build_parent(node, par):
            for neigh in adj[node]:
                if neigh != par:
                    parent[neigh] = node
                    build_parent(neigh, node)

        build_parent(0, -1)

        # Construct Alice's and Bob's directed adjacency lists
        aliceadj = [[] for _ in range(n)]
        bobadj = [[] for _ in range(n)]

        for node in range(1, n):
            p = parent[node]

            aliceadj[p].append(node)  # Parent -> Child
            bobadj[node].append(p)    # Child -> Parent
        bobpath={}
        def dfs(node,parent,time):
            bobpath[node]=time
            if node==0:
                return True
            for neigh in bobadj[node]:
                if neigh != parent:
                    if dfs(neigh,node,time+1):
                        return True
            return False
        dfs(bob,-1,0)
        ans=float('-inf')
        def bfs(node,parent,time,amt):
            nonlocal ans
            
            if node not in bobpath or time<bobpath[node]:
                amt+=amount[node]
            elif time==bobpath[node]:
                amt+=amount[node]//2
            if len(adj[node])==1 and node !=0:
                ans=max(ans,amt)
                return
            for neigh in aliceadj[node]:
                if neigh != parent:
                    bfs(neigh,node,time+1,amt)
        bfs(0,-1,0,0)
        return ans
            