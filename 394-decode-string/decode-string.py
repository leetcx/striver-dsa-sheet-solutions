class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        num=0
        word=""
        for i in range(len(s)):
            if s[i]=='[':
                st.append((word,num))
                word=""
                num=0
                continue
            if s[i]==']':
                prev,n=st.pop()
                word=prev+word*n
                continue
            if s[i].isdigit():
                num=num*10+int(s[i])
            else:
                word+=s[i]
        return word
            
            
            