class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        take=False
        def reg(s,p):
            nonlocal take
            if len(s)==0 and len(p)==0:
                return True
            if  len(p)==0:
                return False
            if len(s) == 0:
                if len(p) > 1 and p[1] == "*":
                    return reg(s, p[2:])
                return False
            if len(p)> 1 and p[1]=="*":
                nottake=reg(s,p[2:])
                if s[0]==p[0] or p[0]==".":
                    take=reg(s[1:],p)
                return take or nottake
            else:
                if s[0]==p[0] or p[0]==".":

                    return reg(s[1:],p[1:])
                
                return False
        return reg(s,p)
