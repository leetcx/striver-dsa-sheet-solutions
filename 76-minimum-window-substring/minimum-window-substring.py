class Solution:
    def minWindow(self, s: str, t: str) -> str:
        set1={}

        for i in t:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        p=len(s)
        d=len(t)
        minlen=float("inf")
        ceta={}
        ans=""
        have=0
        left=0
        for i in range(p):
            if s[i] in ceta:
                ceta[s[i]]+=1
            else:
                ceta[s[i]]=1
            if s[i] in set1 and ceta[s[i]] <= set1[s[i]]:
                have=have+1
            while have==d:
                if i-left+1<minlen:
                    ans=s[left:i+1]
                    minlen=i-left+1
                leftchar=s[left]
                ceta[leftchar]-=1
                if leftchar in set1 and ceta[leftchar] < set1[leftchar]:
                    have-=1
                left+=1
        return ans


