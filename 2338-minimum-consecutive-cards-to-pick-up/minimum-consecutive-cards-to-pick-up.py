class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        low=0
        high=0
        set1={}
        res=float('inf')
        for high in range(len(cards)):
            if cards[high] in set1:
                set1[cards[high]]+=1
            else:
                set1[cards[high]]=1
            
            while set1[cards[high]]>=2 and low<high:
                res=min(res,high-low+1)
                set1[cards[low]]=set1.get(cards[low])-1
                if set1[cards[low]] == 0:
                    del set1[cards[low]]
                low+=1
                
        if res==float('inf'):
            return -1
        return res
            

        