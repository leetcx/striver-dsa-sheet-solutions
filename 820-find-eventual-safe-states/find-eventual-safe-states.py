class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n=len(graph)
        outdeg=[0]* n
        for i in range(n):
            for u in graph[i]:
                outdeg[i]+=1
            
        dict1={}
        for i in range(len(outdeg)):
            if outdeg[i]==0:
                dict1[i]=1
        def dfs(dict1,node,visited,graph,inrecur):
            if node in dict1:
                return True
            visited[node]=True
            inrecur[node]=True
            for neigh in graph[node]:
                if visited[neigh] and inrecur[neigh]:
                    inrecur[node]=False
                    return False
                if visited[neigh]==False and dfs(dict1,neigh,visited,graph,inrecur)==False:
                   
                    inrecur[node]=False
                    return False
               
                    
                
            inrecur[node]=False
            dict1[node]=1
            return True
                    
        ans=[]
        for i in range(n):
            visited=[False] * n
            inrecur=[False] * n
            if dfs(dict1,i,visited,graph,inrecur):
                ans.append(i)   
        return ans