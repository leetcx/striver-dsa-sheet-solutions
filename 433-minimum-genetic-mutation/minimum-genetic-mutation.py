from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q=deque()
        q.append(start)
        level=0
        bank = set(bank)
        visited={start}
        while q:
            n=len(q)
            while n>0:
                str1=q.popleft()
                if str1==end:
                    return level
                for i in "ACGT":
                    for j in range(len(str1)):
                        if i==str1[j]:
                            continue
                        temp=str1[:j]+i+str1[j+1:]
                        if temp in bank and temp not in visited:
                            q.append(temp)
                            visited.add(temp)
                n-=1
            level+=1
        return -1
            



                