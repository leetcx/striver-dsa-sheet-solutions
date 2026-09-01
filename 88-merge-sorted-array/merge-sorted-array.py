class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        arr = nums1[:m]

        low = 0
        low1 = 0

        while low < m and low1 < n:

            if arr[low] < nums2[low1]:
                nums1[low + low1] = arr[low]
                low += 1

            else:
                nums1[low + low1] = nums2[low1]
                low1 += 1

        while low < m:
            nums1[low + low1] = arr[low]
            low += 1

        while low1 < n:
            nums1[low + low1] = nums2[low1]
            low1 += 1
