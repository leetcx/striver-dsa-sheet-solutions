class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for i in range(len(s)):
            if ('a' <= s[i] <= 'z') or ('A' <=s[i] <= 'Z') or ('0' <= s[i] <= '9'):
                new+=s[i].lower()
        low=0
        high=len(new)-1
        while low<high:
            if new[low] != new[high]:
                return False
            low+=1
            high-=1
        return True