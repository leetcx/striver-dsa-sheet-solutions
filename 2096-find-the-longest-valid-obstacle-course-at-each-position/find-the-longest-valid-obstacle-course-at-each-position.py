class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:

        arr=[]
        ans=[] 

        for i in range(len(obstacles)):
            target=obstacles[i]
            low=0
            high=len(arr)-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
                
            if low==len(arr):
                arr.append(obstacles[i])
               
            else:
                arr[low]=obstacles[i]
            ans.append(low+1)
        return ans


      