class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        epsi=0.1
        
        def solve(cards):
            
            if len(cards)==1 and abs(cards[0]-24)<=epsi:
                return True
            for i in range(len(cards)):
                for j in range(len(cards)):
                    if i==j:
                        continue
                    temp=[]
                    for k in range(len(cards)):
                        if k!=i and k !=j:
                            temp.append(cards[k])
                    a=cards[i]
                    b=cards[j]
                    possible=[a+b,a-b,a*b,b-a]
                    if b != 0:
                        possible.append(a / b)

                    if a != 0:
                        possible.append(b / a)
                    for d in possible:
                        temp.append(d)
                        if solve(temp):
                            return True
                        temp.pop()
            return False
        return solve(cards)