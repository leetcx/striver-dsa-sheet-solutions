class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp={}
        def lesdo(i,str1):
            if i==n:
                return 1
            state=(i,str1)
            if state in dp:
                return dp[state]
            take1=0
            take2=0
            take3=0
            take4=0
            take5=0
            if str1=="" or str1=="a":
                take1+=lesdo(i+1,"a")
                take2+=lesdo(i+1,"e")
                take3+=lesdo(i+1,"i")
                take4+=lesdo(i+1,"o")
                take5+=lesdo(i+1,"u")
            elif str1=="e":
                take2+=lesdo(i+1,"e")
                take3+=lesdo(i+1,"i")
                take4+=lesdo(i+1,"o")
                take5+=lesdo(i+1,"u")
            elif str1=="i":
                take3+=lesdo(i+1,"i")
                take4+=lesdo(i+1,"o")
                take5+=lesdo(i+1,"u")
            elif str1=="o":
                take4+=lesdo(i+1,"o")
                take5+=lesdo(i+1,"u")
            else:
                take5+=lesdo(i+1,"u")
            dp[state]= take1+take2+take3+take4+take5
            return dp[state]
        return lesdo(0,"")
            
