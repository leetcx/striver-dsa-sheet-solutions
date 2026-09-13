class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums+=nums
        d=len(nums)
        temp=[-1] * d
        st=[]
        for i in range(len(nums)-1,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                temp[i]=st[-1]
            st.append(nums[i])
        m=d//2
        return temp[:m]