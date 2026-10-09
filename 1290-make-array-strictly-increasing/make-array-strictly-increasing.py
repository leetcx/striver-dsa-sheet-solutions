import bisect



class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        dp={}
        def minimum(i,prev):
            if i>=len(arr1):
                return 0
            state=(i,prev)
            if state in dp:
                return dp[state]
            take=float('inf')
            if  arr1[i]>prev:
                take=minimum(i+1,arr1[i])
            replace=float('inf')
            idx = bisect.bisect_right(arr2, prev)

            if idx < len(arr2):
                val = arr2[idx]
                replace = 1 + minimum(i + 1, val)
            dp[state]= min(take,replace)
            return dp[state]
        p= minimum(0,float('-inf'))
        if p!= float('inf'):
            return p
        return -1
