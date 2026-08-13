class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        temp=[]

        def b(open,close):
            if open==n and close==n:
                ans.append("".join(temp))
            if open<n:
                temp.append('(')
                b(open+1,close)
                temp.pop()
            if close<open:
                temp.append(')')
                b(open,close+1)
                temp.pop()
        b(0,0)
        return ans

