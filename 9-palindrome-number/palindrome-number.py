class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=abs(x)
        def check(x,rev):
            if x<10 :
                return rev*10+x
            rev=rev*10 + x%10
            return check(x//10,rev)
        p=check(x,0)
        return p==original
            
