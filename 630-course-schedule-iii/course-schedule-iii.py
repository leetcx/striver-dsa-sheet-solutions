import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        res=0
        maxheap=[]
        total=0
        for i in range(len(courses)):
            deadline=courses[i][1]
            heapq.heappush(maxheap,-courses[i][0])
            
            total+=courses[i][0]
            if total>deadline:
                longest=-heapq.heappop(maxheap) 
                total-=longest
        return len(maxheap)
            


