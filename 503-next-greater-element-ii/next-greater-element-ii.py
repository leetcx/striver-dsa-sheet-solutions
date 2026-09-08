class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums+=nums
        p=len(nums)
        st=[]
        st.append(nums[-1])
        ans=[0] * p
        for i in range(len(nums)-2,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if not st:
                ans[i]=-1
            else:
                ans[i]=st[-1]
            st.append(nums[i])
        p=p//2
        return ans[:p]
            
