class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp={}
        def scramble(s1,s2):
            if len(s1)==1:
                return s1==s2
            state=(s1,s2)
            if state in dp:
                return dp[state]
            for i in range(1,len(s1)):
                left1=s1[:i]
                right1=s1[i:]
                left2=s2[:i]
                right2=s2[i:]
                notswap=scramble(left1,left2) and scramble(right1,right2)
                swap=scramble(right1,s2[:len(s1)-i]) and scramble(left1,s2[len(s1)-i:])
                if notswap or swap:
                    dp[state]= True
                    return True
            dp[state]= False
            return False
        return scramble(s1,s2)