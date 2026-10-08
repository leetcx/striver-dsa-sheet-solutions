class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:

        arr=[]
        ans=[] 

        for i in range(len(obstacles)):
            pos = bisect_right(arr, obstacles[i])
            if pos==len(arr):
                arr.append(obstacles[i])
               
            else:
                arr[pos]=obstacles[i]
            ans.append(pos+1)
        return ans


      