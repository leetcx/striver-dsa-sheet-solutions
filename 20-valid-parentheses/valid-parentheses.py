class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                st.append(s[i])
            else:
                if not st:
                    return False
                if (st[-1] =='[' and s[i] !=']') or (st[-1] =='{' and s[i] !='}') or (st[-1] =='(' and s[i] !=')') :
                    return False
                st.pop()
        if st:
            return False
        return True
        