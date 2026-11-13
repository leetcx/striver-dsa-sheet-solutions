class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n=len(s1)
        adj=[[] for _ in range(26)]
        for i in range(len(s1)):
            
            adj[ord(s1[i]) - ord('a')].append(s2[i])
            adj[ord(s2[i]) - ord('a')].append(s1[i])
        def dfs(a):
            nonlocal mini
            visited[ord(a) - ord('a')]=True
            idx=ord(a) - ord('a')
            if mini== "" or ord(a)<ord(mini):
                mini=a
           
            for neigh in adj[idx]:
                
                if visited[ord(neigh) - ord('a')]==False:
                    dfs(neigh)
            return mini


        ans=[]

        for p in baseStr:
            visited=[False]*26
            mini=""
            ans.append(dfs(p))
        return "".join(ans)

             