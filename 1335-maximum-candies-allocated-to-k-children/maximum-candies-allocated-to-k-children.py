class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k> sum(candies):
            return 0
        def count(mid):
            k=0
            for i in range(len(candies)):
                k+=candies[i]//mid
            return k
        low=1
        high=max(candies)
        res=-1
        while low<=high:
            mid=(low+high)//2
            if count(mid)<k:
                high=mid-1
            else:
                res=mid
                low=mid+1
        return res
        