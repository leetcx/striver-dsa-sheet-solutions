class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        low=0
        high=len(tokens)-1
        score=0
        p=float('-inf')
        while low<=high:
            if tokens[low] <= power:
                score+=1
                p=max(p,score)
                power-=tokens[low]
                low+=1

            elif score >=1 and tokens[low]> power:
                score-=1
                power+=tokens[high]
                high-=1
            elif score==0 and tokens[low] > power:
                return 0
        if p==float('-inf'):
            return 0
        return p
