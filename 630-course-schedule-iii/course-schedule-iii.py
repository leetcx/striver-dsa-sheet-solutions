import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        idx=0
        day=0
        maxheap=[]
        for i in range(len(courses)):
            day+=courses[i][0]
            heapq.heappush(maxheap,-courses[i][0])
            if maxheap and day > courses[i][1]:
                largest=-heapq.heappop(maxheap)
                day-=largest
        return len(maxheap)
        


