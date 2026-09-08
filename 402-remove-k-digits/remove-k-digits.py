class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        st=[]
       
        for i in range(0,len(num)):
            while st and int(st[-1]) > int(num[i]) and k >0:
                st.pop()
                k-=1
            st.append(num[i])
        while st and k>0:
            st.pop()
            k-=1
        if not st:
            return "0"
        ans=[]
        while st:
            ans.append(st[-1])
            st.pop()
        ans.reverse()
        c=0
        p=""
        for i in range(len(ans)):
            if ans[i]=="0":
                c+=1
            else:
                break
        p="".join(ans)
        if sum(int(x) for x in ans)==0:
            return "0"
        return p[c:len(ans)]
