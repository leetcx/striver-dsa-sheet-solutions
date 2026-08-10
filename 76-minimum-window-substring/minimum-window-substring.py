class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        p=len(t)
        set1={}
        for i in t:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        have=0
        freq={}
        minlen=float("inf")
        left=0
        ans=""
        for i in range(n):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
            if s[i] in set1 and freq[s[i]]==set1[s[i]]:
                have+=1
            while have==len(set1):
                if i-left+1<minlen:
                    minlen=i-left+1
                    ans=s[left:i+1]
                    
                leftchar=s[left]
                freq[leftchar]-=1
                if leftchar in set1 and set1[leftchar]>freq[leftchar]:
                    have-=1
                left+=1
        return ans



