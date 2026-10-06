class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp={}
        def flip(i, choosen1):

            if i >= len(s):
                return 0
            state=(i,choosen1)
            if state in dp:
                return dp[state]
            flip1=float('inf')
            skip1=float('inf')
            if s[i] == "0" and choosen1 == False:
                flip1 = 1+flip(i + 1,  True)
                skip1 = flip(i + 1,  False)
                

            elif s[i] == "0" and choosen1 == True:
                flip1 = 1+flip(i + 1,  True)
                

            elif s[i] == "1" and choosen1 == False:
                flip1 = 1+flip(i + 1,  False)
                skip1 = flip(i + 1,  True)
                
            elif s[i] == "1" and choosen1 == True:
                skip1 = flip(i + 1,  True)
            dp[state]= min(flip1,skip1)
            return dp[state]

        return flip(0, False)