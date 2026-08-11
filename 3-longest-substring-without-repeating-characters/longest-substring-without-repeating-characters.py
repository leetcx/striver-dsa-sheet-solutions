class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        set1=set()
        maxlen=0
        left=0

        for i in s:
            while i in set1:
                set1.remove(s[left])
                left+=1
            set1.add(i)
            maxlen=max(len(set1),maxlen)
        return maxlen
