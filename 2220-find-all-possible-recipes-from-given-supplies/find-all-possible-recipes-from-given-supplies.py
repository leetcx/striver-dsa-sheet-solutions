from collections import deque
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        adj={}
        indegree={}
        
        for i in range(len(recipes)):
            for j in ingredients[i]:
                if j not in adj:
                    adj[j]=[]
                adj[j].append(recipes[i])
                if recipes[i] not in indegree:
                    indegree[recipes[i]]=1
                else:
                    indegree[recipes[i]]+=1
        q=deque(supplies)
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            if node in adj:
                for neigh in adj[node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==0:
                        q.append(neigh)
        return ans[len(supplies):]
        
        
        
           
        
