class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        curr=""
        num=0
        for i in range(len(s)):
            if s[i]=='[':
                st.append((curr,num))
                curr=""
                num=0
                continue
            if s[i]==']':
                if st:
                    prev,n=st.pop()
                    curr=prev+n*curr
                    prev=curr
                    n=num
                else:
                    return curr
            else:
                if s[i].isdigit():
                    num=num*10+int(s[i])
                    continue
                else:
                    curr+=s[i]
        return curr
       