class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans=[] * len(speed)
        for i in range(len(speed)):
            ans.append((position[i],speed[i]))
        ans.sort(key=lambda x:x[0],reverse=True)

        st=[]
        time = (target - ans[0][0]) / ans[0][1]
        st.append(time)
        for i in range(1,len(ans)):
            time1=(target-ans[i][0])/ans[i][1]
            if time1>st[-1]:
                
                
                st.append(time1)
        return len(st)
        