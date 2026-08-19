class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high=max(bloomDay)
        if m*k >len(bloomDay):
            return -1
       
        while low<high:
            
            mid=(low+high)//2
            c=0
            bou=0
            for f in bloomDay:
                if f<=mid:
                    c+=1
                else:
                    c=0
                if c==k:
                    c=0
                    bou+=1
            if bou >= m:
                high = mid

            else:
                low = mid + 1
        return high
