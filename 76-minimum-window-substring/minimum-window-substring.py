class Solution:
    def minWindow(self, s: str, t: str) -> str:
        set1={}
        p=len(t)

        for i in t:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        have=0
        minlen=float("inf")
        d=len(s)
        set2={}
        left=0
        ans=""

        for i in range(len(s)):
            if s[i] in set2:
                set2[s[i]]+=1
            else:
                set2[s[i]]=1
            if s[i] in set1 and set1[s[i]]==set2[s[i]]:
                have=have+1
            while have==len(set1):
                if i-left+1<minlen:
                    minlen=i-left+1
                    ans=s[left:i+1]
                leftchar=s[left]
                set2[leftchar]-=1
                if leftchar in set1 and set2[leftchar] < set1[leftchar]:
                    have -= 1

                left += 1
        return ans
                