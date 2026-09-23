class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        temp=["("]
        balance=1
        open=1
        ans=[]
        def solve():
            nonlocal temp
            nonlocal ans 
            nonlocal open
            nonlocal balance
            if len(temp)==2*n:
                ans.append("".join(temp.copy()))
                return
            if open<n:
                temp.append("(")
                balance+=1
                open+=1
                solve()
                temp.pop()
                balance-=1
                open-=1
            if balance>0:
                temp.append(")")
                balance-=1
                
                solve()
                temp.pop()
                balance+=1
        solve()
        return ans
        

                


