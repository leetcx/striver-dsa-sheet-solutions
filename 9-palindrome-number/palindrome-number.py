class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1=str(x)
        i=0
        j=len(s1)-1
        while i<j:
            if s1[i] != s1[j]:
                return False
            i+=1
            j-=1
        return True
            