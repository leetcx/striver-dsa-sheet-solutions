class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        dp={}
        def partition(i):
            if i>=len(s):
                return 1
            state=i
            if state in dp:
                return dp[state]
            take=0
            for j in range(i,min((i+2),len(s))):
                parti=s[i:j+1]
                if parti[0] != "0" and len(parti) <=2 and int(parti)>0 and int(parti)<=26:
                    take+=partition(j+1)
            dp[state]= take
            return take
        return partition(0)
                