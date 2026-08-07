class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count=0
        def mergeSort(low,high):
            if low>=high:
                return
            mid=(low+high)//2
            mergeSort(low,mid)
            mergeSort(mid+1,high)

            j=mid+1
            n=len(nums)

            for i in range(low,mid+1):
                while j<=high and nums[i]>2*nums[j]:
                    j+=1
                self.count+=j-(mid+1)

            left=low
            right=mid+1
            temp=[]


            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                elif nums[right]<nums[left]:
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while right<=high:
                temp.append(nums[right])
                right+=1
            nums[low:high+1]=temp
        mergeSort(0,len(nums)-1)
        return self.count

