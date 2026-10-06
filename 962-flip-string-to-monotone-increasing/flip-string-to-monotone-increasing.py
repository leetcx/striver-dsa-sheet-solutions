class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones=0
        flip=0
        for i in range(len(s)):
            if s[i]=="1":
                ones+=1
            elif s[i]=="0" and ones>0:
                flip=min(flip+1,ones) 
            
        return flip   