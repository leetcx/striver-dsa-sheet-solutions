import heapq
class MedianFinder:

    def __init__(self):
        self.leftheap=[]
        self.rightheap=[]

    def addNum(self, num: int) -> None:
        if not self.leftheap:
            heapq.heappush(self.leftheap,-num)
        elif num>-self.leftheap[0]:
            heapq.heappush(self.rightheap,num)
        else:
            heapq.heappush(self.leftheap,-num)
        diff=abs(len(self.leftheap)-len(self.rightheap))
        if diff>1:
            if len(self.leftheap) > len(self.rightheap):
                d=-heapq.heappop(self.leftheap)
                heapq.heappush(self.rightheap,d)
            else:
                p=heapq.heappop(self.rightheap)
                heapq.heappush(self.leftheap,-p)



    def findMedian(self) -> float:
        if len(self.leftheap)==len(self.rightheap):
            t=-self.leftheap[0]
            z=self.rightheap[0]
            self.d=(t+z)/2
        elif len(self.leftheap) > len(self.rightheap):
            self.d=-self.leftheap[0]
        else:
            self.d=self.rightheap[0]
        return self.d
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()