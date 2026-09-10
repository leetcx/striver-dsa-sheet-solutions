import heapq
class Pair:
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency < other.frequency
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        minheap=[]
        set1={}
        for i in words:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for element,frequency in set1.items():
            if len(minheap) < k:
                heapq.heappush(minheap,Pair(frequency,element))
            else:
                if (frequency > minheap[0].frequency):
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,Pair(frequency,element))
                elif frequency == minheap[0].frequency:
                    if element < minheap[0].word:
                        heapq.heappop(minheap)
                        heapq.heappush(minheap, Pair(frequency, element))
        res=[]
        while minheap:
            res.append(minheap[0].word)
            heapq.heappop(minheap)
        res.reverse()
        return res
