class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        max1=float('inf')
        temp=[0] * k
        ans=0
        def cal(i,k,cookies):
            nonlocal ans
            nonlocal temp
            nonlocal max1
            if i >= len(cookies):
                if max1> max(temp):
                    max1=max(temp)
                    ans=max(temp)
                return 
            for j in range(k):
                temp[j]+=cookies[i]
                cal(i+1,k,cookies)
                temp[j]-=cookies[i]
        cal(0,k,cookies)
        return ans

                