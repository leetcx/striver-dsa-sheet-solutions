class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n=len(edges)
        visited=[False]* n
        count=[1]*n
        inrecur=[False] * n
        def dfs(node,edges):
            if node!=-1:
                visited[node]=True
                inrecur[node]=True
                neigh=edges[node]
            
                if neigh!=-1 and visited[neigh]==True and inrecur[neigh]==True:
                    ans=count[node]-count[neigh]+1
                    inrecur[node]=False
                    return ans
                elif neigh!=-1 and visited[neigh]==False :
                    count[neigh]=count[node]+1
                    ans= dfs(neigh,edges)
                    inrecur[node]=False
                    return ans
                inrecur[node]=False
            return -1
            
        result=-1
        for i in range(n):
            if visited[i]==False:
               
                result=max(result,dfs(i,edges))
                
        return result 


        