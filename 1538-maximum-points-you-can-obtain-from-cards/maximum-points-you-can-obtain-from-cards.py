class Solution:
    def maxScore(self, car: List[int], k: int) -> int:
        p=len(car) -k
        res=float('inf')  
        low=0
        high=p-1
        g=sum(car[low:high+1])
       
        while high < len(car):
            res=min(res,g)
            if high >= len(car) - 1:
                break
            g=g-car[low]
            low+=1
            high+=1
            
            g=g+car[high]
            
        y=sum(car)-res
        return y