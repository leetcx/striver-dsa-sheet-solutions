class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        best=arr[0]
        ans=arr[0]
        for i in range(1,len(arr)):
            best=max(arr[i],best+arr[i])
            ans=max(ans,best)
        
        if ans<0:
            return 0
        if k==1:
            return ans
        sum1=0
        res=float('-inf')
        for i in range(len(arr)):
            sum1+=arr[i]
            res=max(res,sum1)
        sum2=0
        rise=float('-inf')
        for i in range(len(arr)-1,-1,-1):
            sum2+=arr[i]
            rise=max(rise,sum2)

       
        if sum(arr)>0:
            ans=max(ans,res+rise+(sum(arr)*(k-2))) % (10**9 + 7)

            return ans
        else:
            return max(ans,res+rise)
        