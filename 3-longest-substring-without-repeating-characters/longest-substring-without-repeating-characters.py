class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high =0
        res=float('-inf')
        set1={}
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            while high-low+1>len(set1):
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
            res=max(res,high-low+1)
        if res==float('-inf'):
            return 0
        return res