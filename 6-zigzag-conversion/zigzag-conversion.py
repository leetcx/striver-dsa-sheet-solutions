class Solution:
    def convert(self, s: str, numRows: int) -> str:
        currow=0
        n=len(s)
        goingdown=True
        ans=[""] *n
        for i in s:
            ans[currow]+=i

            if currow==numRows-1:
                goingdown=False
            if currow==0:
                goingdown=True
            if goingdown==True:
                currow+=1
            else:
                currow-=1
        return "".join(ans)
            

