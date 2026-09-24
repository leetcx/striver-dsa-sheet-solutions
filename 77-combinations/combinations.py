class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        copy=[0] * n
        for i in range(n):
            copy[i]=i+1
        ans=[]
        temp=[]
        def solve(j,p):
            nonlocal temp
            nonlocal ans 
            nonlocal copy
            if j==k:
                ans.append(temp.copy())
                return 
            for i in range(p,len(copy)):
                temp.append(copy[i])
                solve(j+1,i+1)
                temp.pop()
        solve(0,0)
        return ans