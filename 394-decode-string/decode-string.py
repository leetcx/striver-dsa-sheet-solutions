class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        word=""
        st=[]
        t=len(s)
        i=0
        while i<t:
            if s[i]=='[':
                st.append((word,num))
                word=""
                num=0
                i+=1
            elif st and s[i]==']':
                prev,n=st.pop()
                word=prev+ n * word
                prev=word
                i+=1
            else:
                if s[i].isdigit():
                    num=num*10 + int(s[i])
                    i+=1
                elif s[i].isalpha():
                    word+=s[i]
                    i+=1


        return word
                