class Solution:
    def convert(self, s: str, numRows: int) -> str:
        currows=0
        n=len(s)
        ans=[""] *n
        if numRows==1:
            return s

        goingdown=True

        for i in s:
            ans[currows]+=i

            if currows==0:
                goingdown=True
            if currows==numRows-1:
                goingdown=False
            if goingdown==True:
                currows+=1
            else:
                currows-=1
        return "".join(ans)