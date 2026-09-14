class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1={}
        res=float('-inf')
        low=0
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            while len(set1)<high-low+1 and low<=high:
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
            res=max(res,high-low+1)
        if res==float('-inf'):
            return 0
        return res
