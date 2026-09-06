class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ans=[0] * len(nums2)
        st=[]
        st.append(nums2[-1])
        ans[-1]=-1
        pou=[]
        for i in range(len(nums2)-2,-1,-1):
            while st and nums2[i] >=st[-1]:
                st.pop()
            if not st:
                ans[i]=-1
            else:
                ans[i]=st[-1]
            st.append(nums2[i])
        an = []

        for x in nums1:
            index = nums2.index(x)
            an.append(ans[index])
        return an
            
                   
            
                