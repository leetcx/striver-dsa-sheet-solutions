class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
            st1=[]
            st2=[]
            l=len(s)
            p=len(t)
            for i in range(l):
                if s[i] != '#':
                    st1.append(s[i])
                else:
                    if st1:
                        st1.pop()
            for j in range(p):
                if t[j] != '#':
                    st2.append(t[j])
                else:
                    if st2:
                        st2.pop()
            if st1==st2:
                return True
            return False
            