class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in range(0,len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                st.append(tokens[i])
                continue
            else:
                a=st.pop()
                b=st.pop()
                if tokens[i]=='+':
                    res=int(a)+int(b)
                if tokens[i]=='-':
                    res=int(b)-int(a)
                if tokens[i]=='*':
                    res=int(a)*int(b)
                if tokens[i]=='/':
                    res=int(b)/int(a)
            st.append(res)
        p=0
        while st:
            p=p*10+int(st[-1])
            st.pop()
        return p
