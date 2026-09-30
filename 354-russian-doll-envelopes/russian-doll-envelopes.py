class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
       
        tails=[]
        for i in envelopes:
            p=i[1]
            pos=bisect_left(tails,p)
            if pos==len(tails):
                tails.append(p)
            else:
                tails[pos]=p
            
        return len(tails)