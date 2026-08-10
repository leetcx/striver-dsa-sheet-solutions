class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        low=1
        high=max(piles)

        while low<high:
            mid=(low+high)//2
            hours=0

            for i in piles:
                hours+=(i+mid-1)//mid

            if hours<=h:
                high=mid
            else:
                low=mid+1
        return high
