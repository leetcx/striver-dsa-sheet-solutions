class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
       
        
        b = float('-inf')
        st = []

        for i in range(len(nums)-1, -1, -1):

            if nums[i] < b:
                return True

            while st and st[-1] < nums[i]:
                b = st.pop()

            st.append(nums[i])
        return False