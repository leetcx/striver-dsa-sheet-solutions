class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp=[]
        ans =[]
        def backtrack(open,close,n):
            if open==n and close==n:
                ans.append("".join(temp))
            if open<n:
                temp.append('(')
                backtrack(open+1,close,n)
                temp.pop()
            if close<open:
                temp.append(')')
                backtrack(open,close+1,n)
                temp.pop()
        backtrack(0,0,n)
        return ans
