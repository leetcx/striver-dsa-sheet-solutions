class Solution:
    def validPalindrome(self, s: str) -> bool:
        low=0
        high=len(s)-1
        key=1
        while low<high:
            if s[low]!=s[high]:
                l1=low+1
                h2=high
                while l1<h2:
                    if s[l1] != s[h2]:
                        break
                    l1+=1
                    h2-=1
                if l1>=h2:
                    return True
                l2=low
                h1=high-1
                while l2<h1:
                    if s[l2] != s[h1]:
                        return False
                    l2+=1
                    h1-=1
                return True
            low+=1
            high-=1
        return True
      