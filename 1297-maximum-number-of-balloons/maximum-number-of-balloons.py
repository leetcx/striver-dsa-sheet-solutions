class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        set1={}
        for i in 'balloon':
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        set2={}
        for j in text:
            if j in set2:
                set2[j]+=1
            else:
                set2[j]=1
        c=0
        while all(key in set2 and set2[key] >= value for key, value in set1.items()):
            set2['b']-=1
            set2['a']-=1
            set2['l']-=1
            set2['l']-=1
            set2['o']-=2
            set2['n']-=1
            c+=1
        return c

