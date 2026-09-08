class Solution:
    def longestPalindrome(self, s: str) -> int:
        set1={}
        ans=0
        odd=0
        for i in s:

            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for i in s:
            if i in set1 and set1[i] % 2==0:
                ans+=set1[i]
                del set1[i]
        for i in s:
            if i in set1 and set1[i] % 2==1:
                odd=1
                ans+=set1[i]-1
                del set1[i]
        if odd:
            ans+=1
        return ans
        