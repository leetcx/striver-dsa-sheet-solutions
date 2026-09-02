class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                news += s[i].lower()

        
        low=0
        high=len(news)-1
        while low<high:
            if news[low] != news[high]:
                return False
            low+=1
            high-=1
        return True