class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n=len(nums)
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        intime=[0] * n
        outtime=[0]*n
        xorsubtree=[0] * n
        timer=0
        def getscore(u,v,w):
            z=max(u,v,w)
            p=min(u,v,w)
            return z-p
        def isancestor(u,v,intime,outtime):
            if intime[u]<=intime[v] and outtime[v]<=outtime[u]:
                return True
            return False

        def dfs(node,parent,intime,outtime,xorsubtree):
            nonlocal timer
            intime[node]=timer
            timer+=1
            xorsubtree[node]=nums[node]
            for neigh in adj[node]:
                if neigh != parent:
                    dfs(neigh,node,intime,outtime,xorsubtree)
                    xorsubtree[node]^=xorsubtree[neigh]
            outtime[node]=timer
            timer+=1
        dfs(0,-1,intime,outtime,xorsubtree)
        result=float('inf')
        for i in range(1,n):
            for j in range(i+1,n):
                if isancestor(i,j,intime,outtime):
                    xor1=xorsubtree[j]
                    xor2=xorsubtree[i] ^ xor1
                    xor3=xorsubtree[0] ^ xor1 ^ xor2
                elif isancestor(j,i,intime,outtime):
                    xor1=xorsubtree[i]
                    xor2=xorsubtree[j] ^ xor1
                    xor3=xorsubtree[0] ^ xor1 ^ xor2
                else:
                    xor1=xorsubtree[i]
                    xor2=xorsubtree[j] 
                    xor3=xorsubtree[0] ^ xor1 ^ xor2
                result=min(result,getscore(xor1,xor2,xor3))
        return result

