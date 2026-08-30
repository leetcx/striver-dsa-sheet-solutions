class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        p=len(words)
        map1={}
        
        ans=[]
        if p==0:
            return []
        g=len(words[0])
        t=p*g
        if t> len(s):
            return []
        for word in words:
            if word in map1:
                map1[word]+=1
            else:
                map1[word]=1
        for start in range(g):
            low=start
            high=start + t -1
            map2={}

            if high>=len(s):
                break
            for i in range(start, start + t, g):
                word = s[i:i+g]

                if word in map2:
                    map2[word] += 1
                else:
                    map2[word] = 1

            while high<len(s) and low<len(s):
                if map1==map2:
                    ans.append(low)
                word=s[low:low+g]
                map2[word]=map2.get(word,0)-1

                if map2[word]==0:
                    del map2[word]
                low+=g
                high+=g
                if high>= len(s):
                    break
                wordu=s[high-g+1:high+1]
                map2[wordu]=map2.get(wordu,0)+1
        return ans

        
