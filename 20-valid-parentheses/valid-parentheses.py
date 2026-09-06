class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        st=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                st.append(s[i])
            else:
                if not st:
                    return False
                if (s[i]==')' and st[-1] !='(') or  (s[i]=='}' and st[-1] !='{') or (s[i]==']' and st[-1] !='['):
                    return False
                else:
                    st.pop()
        if  st:
            return False
        return True