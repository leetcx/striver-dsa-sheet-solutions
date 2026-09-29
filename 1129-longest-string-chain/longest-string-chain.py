class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        maxlen=float('-inf')
        words.sort(key=len)
        t = [[-1] * (len(words) + 1) for _ in range(len(words))]
        def isvalid(str1,str2):
            if len(str1)-len(str2) !=1:
                return False
            i=0
            j=0
            diff=0
            while i<len(str1) and j<len(str2):
                if str1[i] != str2[j]:
                    diff+=1
                    i+=1
                    if diff>1:
                        return False
                else:
                    i+=1
                    j+=1
                
            return True
        count=0
        ans=1
        def maxii(i,prev):
            nonlocal t
            if i>=len(words):
                
                return 0
            if prev != -1 and t[i][prev] != -1:
                return t[i][prev]
            take=0
            if prev==-1 or isvalid(words[i],words[prev]):
                take=1+maxii(i+1,i)
                skip=maxii(i+1,prev)
            else:
                skip=maxii(i+1,prev)
            if prev != -1:
                t[i][prev]=max(take,skip)
            return max(take,skip)
        return maxii(0,-1)
       

