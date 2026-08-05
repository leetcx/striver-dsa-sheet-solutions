class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
           nums1.append(i)

        nums1.sort()

        n = len(nums1)
        l = 0
        r = n - 1
        mid =  n // 2

        if n % 2 == 1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid - 1]) / 2