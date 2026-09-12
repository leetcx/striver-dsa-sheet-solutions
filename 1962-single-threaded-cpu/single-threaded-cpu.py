import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        arr=[]
        minheap=[]
        for i in range(len(tasks)):
            arr.append((tasks[i][0],tasks[i][1],i))
        arr.sort()
        g=0
        p=0
        res=[]
        while len(res) < len(tasks):
            if not minheap:
                g=max(g,arr[p][0])
            while p<n and g>=arr[p][0]:
                enqueue, process, idx = arr[p]
                heapq.heappush(minheap,(process,idx))
                p+=1
            tou,indi=heapq.heappop(minheap)
            res.append(indi)
            g+=tou
        return res

        9