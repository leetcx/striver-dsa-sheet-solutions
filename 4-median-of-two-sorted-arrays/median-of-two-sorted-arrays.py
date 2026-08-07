class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2):
            nums1,nums2=nums2,nums1
        l=0
        n1=len(nums1)
        n2=len(nums2)
        r=n1
        while l<=r:
            cut1=(l+r)//2
            cut2=(n1+n2+1)//2-cut1

            if cut1==0:
                l1=float("-inf")
            else:
                l1=nums1[cut1-1]
            if cut1==n1:
                r1=float("inf")
            else:
                r1=nums1[cut1]
            if cut2==0:
                l2=float("-inf")
            else:
                l2=nums2[cut2-1]
            if cut2==n2:
                r2=float("inf")
            else:
                r2=nums2[cut2]
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==0:
                    return (max(l1,l2)+ min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1>r2:
                r=cut1-1
            else:
                l=cut1+1      
