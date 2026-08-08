class Solution:
    def dailyTemperatures(self, st1: List[int]) -> List[int]:
        s1=[]
        n=len(st1)
        ans=[0]*n

        for i in range(n-1,-1,-1):
            while s1 and st1[i]>=st1[s1[-1]]:
                s1.pop()
            if s1:
                ans[i]=s1[-1]-i
            s1.append(i)
        return ans
        
        