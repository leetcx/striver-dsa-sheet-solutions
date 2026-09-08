class Solution:
    def firstUniqChar(self, s: str) -> int:
        set1={}
        for i in range(len(s)):
            if s[i] in set1:
                set1[s[i]]+=1
            else:
                set1[s[i]]=1
        for key,value in set1.items():
            if value==1:
                return s.index(key)
        return -1


