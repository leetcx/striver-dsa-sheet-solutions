class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n=len(bills)
        five=0
        ten=0
        for i in range(0,n):
            money=bills[i]
            if money==5:
                five+=1
            elif money==10:
                if five==0:
                    return False
                five-=1
                ten+=1
            elif money == 20:

                if ten>0:
                    ten-=1
                    if five==0:
                        return False
                    five-=1
                elif five<3:
                    return False
                else:
                    five=five-3
        return True