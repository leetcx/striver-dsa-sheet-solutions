class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        set1={}
        for i in range(len(allowed)):
            d=allowed[i][0]+allowed[i][1]
            
            if d not in set1:
                set1[d] = []

            set1[d].append(allowed[i][2])
        curr=bottom
        def check(curr,pq,i):
            if len(curr)==1:
                return True
            if i==len(curr)-1:
                return check(pq,"",0)
            pair=curr[i:i+2]
            if pair not in set1:
                return False
            for ch in set1[pair]:
                pq+=ch
                if check(curr,pq,i+1):
                    return True
                pq=pq[:-1]
            return False
        return check(bottom,"",0)

            
        
