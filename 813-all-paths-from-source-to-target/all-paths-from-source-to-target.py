class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans=[]
        n=len(graph)
        visited=[False] * len(graph)
        ans.append(0)
        visited[0]=True
        result=[]
        temp=[0]
        def dfs(node,adj):
            nonlocal result
            nonlocal temp
            if node==n-1:
                result.append(temp.copy())
                return
            for neigh in adj[node]:
                if visited[neigh]==False:
                    temp.append(neigh)
                    dfs(neigh,adj)
                    temp.pop()
        dfs(0,graph)
        return result
            