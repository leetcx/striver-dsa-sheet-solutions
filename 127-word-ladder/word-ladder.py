from collections import deque
class Solution:
    def ladderLength(self, begin: str, end: str, wordlist: List[str]) -> int:
        n=len(wordlist)
        set1={}      
        q=deque()  
        for i in range(n):
            set1[wordlist[i]]=1
        if begin not in set1:
            set1[begin]=1
        if end not in set1:
            return 0
        q.append((begin,1))
        set1.pop(begin)
        while q:
            s,val=q.popleft()
            if s== end:
                return val
            for i in range(len(s)):
                c=s[i]
                for j in range(97,123):
                    if c==chr(j):
                        continue
                    neword=s[:i] + chr(j) + s[i+1:]
                    if neword in set1:
                        q.append((neword,val+1))
                        set1.pop(neword)
               
        return 0
        