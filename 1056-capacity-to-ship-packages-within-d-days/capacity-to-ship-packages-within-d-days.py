class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)

        while low<=high:
            mid=(low+high)//2

            day=1
            thuu=0
            for i in weights:
                if thuu+i>mid:
                    day+=1
                    thuu=i
                else:
                    thuu=thuu+i
            if day<=days:
                high=mid-1
            else:
                low=mid+1
        return low

