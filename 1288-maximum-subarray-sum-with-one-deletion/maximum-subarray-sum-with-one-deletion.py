class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete=arr[0]
        onedelete=0
        res=arr[0]
        for i in range(1,len(arr)):
            prev=nodelete
            nodelete=max(arr[i],nodelete+arr[i])
            onedelete=max(onedelete+arr[i],prev)
            res=max(res,onedelete,nodelete)
        return res