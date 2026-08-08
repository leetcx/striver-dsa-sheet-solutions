class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        n=len(a)
        st=[]

        for i in range(n):
            
            while st and st[-1]>0 and a[i]<0:
                sum=st[-1]+a[i]
                if sum==0:
                    st.pop()
                    break
                elif sum>0:
                    break
                elif sum<0:
                    st.pop()
            else:
                st.append(a[i])
        return st