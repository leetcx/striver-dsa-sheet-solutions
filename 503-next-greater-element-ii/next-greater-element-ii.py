class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums+=nums
        p=len(nums)
        res=[-1] * p
        st=[]
        for i in range(p-1,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                res[i]=st[-1]
            st.append(nums[i])
        z=p//2
        return res[:z]