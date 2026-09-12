import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extrastudents: int) -> float:
        minheap=[]
        for i in range(len(classes)):
            rat=((classes[i][0]+1)/(classes[i][1]+1))-(classes[i][0]/classes[i][1])
            heapq.heappush(minheap,(-rat,i))
        while extrastudents > 0:
            t, idx = heapq.heappop(minheap)

            classes[idx][0] += 1
            classes[idx][1] += 1

            rat = ((classes[idx][0] + 1) / (classes[idx][1] + 1)) - (classes[idx][0] / classes[idx][1])

            heapq.heappush(minheap, (-rat, idx))

            extrastudents -= 1
        rat = 0

        for passed, total in classes:
            rat += passed / total

        return rat / len(classes)