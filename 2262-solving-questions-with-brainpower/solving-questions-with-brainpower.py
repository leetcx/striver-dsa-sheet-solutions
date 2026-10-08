class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp={}
        def cal(i):
            if i>=len(questions):
                return 0
            state=i
            if state in dp:
                return dp[state]
            take=questions[i][0]+cal(i+questions[i][1]+1)
            skip=cal(i+1)
            dp[state]= max(take,skip)
            return dp[state]
        return cal(0)