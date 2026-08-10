class Solution:
    def decodeString(self, s: str) -> str:
        stringstack=[]
       
        p=len(s)

        for i in range (p):
            if s[i]!=']':
                stringstack.append((s[i]))
            else:
        
            
                t=""
                while stringstack and stringstack[-1]!='[':
                    t=stringstack.pop()+t
                stringstack.pop()
                k=""
                while stringstack and stringstack[-1].isdigit():
                    k=stringstack.pop() + k
                stringstack.append((t*(int(k))))
        return "".join(stringstack)

                
