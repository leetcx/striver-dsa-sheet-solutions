class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        low=0
        high=k-1
        count=0
        p=sum(arr[low:high+1])
        while high<len(arr):
            avg=p//(high-low+1)
            if avg>=threshold:
                count+=1
            p=p-arr[low]
            low+=1
            high+=1
            if high>= len(arr):
                break
            p=p+arr[high]
        return count