class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        ans=""
        started=False
        for i in range(n):
            if s[i]==" " and not started:
                continue
            if (s[i]=='+' or s[i]=='-') and not started:
                ans+=s[i]
                started=True
               
            elif s[i].isdigit():
                ans+=s[i]
                started=True
            else:
                break
        if ans=="" or ans=='-' or ans=='+':
            return 0
        sign=1
        if ans[0]=='-':
            sign=-1
        num=0
        for ch in ans:
            if ch == '+' or ch == '-':
                continue

            num = num * 10 + (ord(ch) - ord('0'))
        num*=sign
        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num
