class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        st1=[]
        ans=[0] * n
        for i in range(n-1,-1,-1):
            while st1 and temp[st1[-1]] <= temp[i]:
                st1.pop()
            if st1:
                ans[i]=st1[-1]- i
            st1.append(i)
        return ans
