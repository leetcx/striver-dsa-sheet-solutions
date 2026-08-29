class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        dic={}
        n=len(arr)
        low=0
        high=n-1    
        for i in range(n):
            if arr[low] + arr[high] ==target:
                return[low+1,high+1]
            if arr[low] + arr[high] > target:
                high-=1
            elif arr[low] + arr[high] < target:
                low+=1
        