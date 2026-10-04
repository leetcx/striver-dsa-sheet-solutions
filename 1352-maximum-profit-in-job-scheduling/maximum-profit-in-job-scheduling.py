class Solution:
    def jobScheduling(self, starttime: list[int], endtime: list[int], profit: list[int]) -> int:
        jobs = []

        for i in range(len(starttime)):
                jobs.append([starttime[i], endtime[i], profit[i]])
        jobs.sort()
        marked=[False] * len(starttime)
        dp={}
        def getnext(arr,low,target):
            high=len(arr)-1
            result=len(arr)+1
            while low<=high:
                mid=(low+high)//2
                if arr[mid][0]>=target:
                    result=mid
                    high=mid-1
                else:
                    low=mid+1
            
            return result
        dp={}
        def solve(jobs,i):
            nonlocal marked
            if i>=len(jobs):
                return 0
            if i in dp:
                return dp[i]
            next1= getnext(jobs,i+1,jobs[i][1])
            take=jobs[i][2] + solve(jobs,next1)
                
            skip=solve(jobs,i+1)
            dp[i]= max(take,skip)
            return dp[i]
             
        return solve(jobs,0)

            