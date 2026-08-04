class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minspeed=1
        maxspeed=max(piles)
        hours=0
        
        while minspeed< maxspeed:
            mid=(minspeed+maxspeed)//2
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if hours<=h:
                maxspeed=mid
            else:
                minspeed=mid+1
        return maxspeed

            

