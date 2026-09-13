class Solution:
    def minEatingSpeed(self, piles: List[int], ho: int) -> int:
        def find(mid):
            h=0
            for i in piles:
                t=i%mid
                d=i//mid
                if t>0:
                    h+=d+1
                else:
                    h+=d
            return h
        low=1
        high=max(piles)
        res=0
        while low<=high:
            mid=(low+high)//2
            c=find(mid)
            if c<=ho:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
        