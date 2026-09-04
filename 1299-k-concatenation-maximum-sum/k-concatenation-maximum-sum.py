class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        best=0
        res=0
        for i in range(len(arr)):
            best=max(best + arr[i],arr[i])
            res=max(res,best)
        if k==1:
            return res
        total=sum(arr)
        bestpre=float('-inf')
        sum1=0
        for i in range(len(arr)):
            sum1+=arr[i]
            bestpre=max(bestpre,sum1)
        bestsuff=float('-inf')
        sum1=0
        for i in range(len(arr)-1,-1,-1):
            sum1+=arr[i]
            bestsuff=max(bestsuff,sum1)
        if total<=0:
            return max(res,bestsuff+bestpre)
        else:
            return max(res, bestsuff + (k-2)*total + bestpre) % (10**9 + 7)
            
            
            