from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set1={}
        for i in range(len(wordList)):
            set1[wordList[i]]=1
        
        if endWord not in set1:
            return 0
        q=deque()
        q.append((beginWord,1))
        

        while q:
            string,val=q.popleft()
            if string==endWord:
                return val
            p=len(string)
            for i in range(p):
                c=string[i]
                for j in range(97,123):
                    if c== chr(j):
                        continue
                    new=string[:i] + chr(j)+string[i+1:]
                    if new in set1:
                        q.append((new,val+1))
                        set1.pop(new)
                
        return 0