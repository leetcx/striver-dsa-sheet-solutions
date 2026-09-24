class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        temp=""
        ans=[]
        def partition(s,wordDict):
            nonlocal ans
            nonlocal temp
            if len(s)==0:
                ans.append(temp.strip())
                return 
            for i in range(len(s)):
                z=s[0:i+1]
            
                if z in wordDict:
                    temp+=z+" "
                    partition(s[i+1:],wordDict)
                    temp=temp[:-(len(z) + 1)]
        partition(s,wordDict)
        return ans
            