class Solution:
    def maxScore(self, car: List[int], k: int) -> int:
        p=len(car) -k
        res=float('inf')  
        low=0
        high=p-1
        g=sum(car[low:high+1])
        res=min(res,g)
        while high < len(car)-1:
            
            g=g-car[low]
            low+=1
            high+=1
            if high>=len(car):
                break
            g=g+car[high]
            res=min(res,g)
        y=sum(car)-res
        return y