class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        set1={}
        for i in range(len(letters)):
            if letters[i] in set1:
                set1[letters[i]]+=1
            else:
                set1[letters[i]]=1
        maxscore=0
        def solve(curscore,i,set1):
            nonlocal maxscore
            if i==len(words):
                maxscore=max(curscore,maxscore)
                return
            temp=set1.copy()
            tempscore=0
            possible=True
            for j in range(len(words[i])):
                if words[i][j] not in temp or temp[words[i][j]]==0:
                    possible=False
                    break
                temp[words[i][j]]-=1
                tempscore+=score[ord(words[i][j]) - ord('a')]
                
            if possible:
                solve(curscore+tempscore,i+1,temp)
           
            solve(curscore,i+1,set1)
        solve(0,0,set1)
        return maxscore

                


