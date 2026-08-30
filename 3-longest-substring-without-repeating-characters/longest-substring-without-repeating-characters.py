class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seto={}
        low=0
        high=0
        maxi=float('-inf')
        for high in range(0,len(s)):
            if s[high] in seto:
                seto[s[high]]+=1
            else:
                seto[s[high]]=1
            k=high-low+1
            while k!=len(seto):
                seto[s[low]]-=1
                if seto[s[low]]==0:
                    del seto[s[low]]
                low+=1
                k=high-low+1
            if k==len(seto):
                maxi=max(maxi,k)
        if maxi==float(-inf):
            return 0
        return maxi