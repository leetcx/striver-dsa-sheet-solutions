class Solution:
    def integerBreak(self, n: int) -> int:
        arr=[]
        for i in range(1,n):
            arr.append(i)
        dp={}
        def maxii(i,n,k):
            if i>=len(arr):
                if n==0 and k>=2:
                   
                    return 1
                   
                return 0
            if n<0:
                return 0
            state=(i,n,k)
            if state in dp:
                return dp[state]
            take=float('-inf')
            if n>=arr[i]:
                take=arr[i]*maxii(i,n-arr[i],k+1)
            skip=maxii(i+1,n,k)
            dp[state]= max(take,skip)
            return dp[state]
        return maxii(0,n,0)
