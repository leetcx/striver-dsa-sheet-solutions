class Solution:
    def minDays(self, bloomday: List[int], m: int, k: int) -> int:
        if m*k > len(bloomday):
            return -1
        low=min(bloomday)
        high=max(bloomday)
        c=0
        bou=0

        while low<high:
            mid=(low+high)//2

            c=0
            bou=0

            for i in range(len(bloomday)):
                if mid >= bloomday[i]:
                    c+=1
                else:
                    c=0
                    
                if c==k:
                    c=0
                    bou+=1
            if bou<m:
                low=mid+1
            else:
                high=mid
        return high