class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n=len(strs)
        adj=[[] for _ in range(n)]  
        def issimilar(s1,s2):
            if len(s1) != len(s2):
                return False
            c=0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    c+=1
            if c>2:
                return False
            return True
        for i in range(n):
            for j in range(i+1,n):
                if issimilar(strs[i],strs[j]):
                    adj[i].append(j)  
                    adj[j].append(i)
        def dfs(node):
            visited[node]=True
            for neigh in adj[node]:
                if visited[neigh]==False:
                    dfs(neigh)
        visited=[False] * n
        ans=0
        for j in range(n):
            if visited[j]==False:
                ans+=1
                dfs(j)
        return ans
                
            
                