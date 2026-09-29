class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        maxlen=float('-inf')
        words.sort(key=len)
        t = [1] * len(words)
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
        for i in range(len(words)):
            for j in range(i):
                if isvalid(words[i],words[j]):
                    t[i]=max(t[j]+1,t[i])
                    maxlen=max(maxlen,t[i])
        if maxlen==float('-inf'):
            return 1
        return maxlen
