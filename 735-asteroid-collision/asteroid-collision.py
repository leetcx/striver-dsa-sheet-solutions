class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        st=[]
        
        st.append(nums[0])
        for i in range(1,len(nums)):
            if not st:
                st.append(nums[i])
                continue

            if (st[-1] > 0 and nums[i] > 0) or \
               (st[-1] < 0 and nums[i] > 0) or \
               (st[-1] < 0 and nums[i] < 0):
                st.append(nums[i])
                continue

            while st and st[-1] >0 and nums[i]<0:
                if abs(st[-1]) < abs(nums[i]):
                    st.pop()
                    continue
                elif abs(st[-1]) == abs(nums[i]):
                    st.pop()
                    break
                else:
                    break
            else:
                st.append(nums[i])

        ans=[]
        while st:
            ans.append(st[-1])
            st.pop()
        ans.reverse()
        return ans
            