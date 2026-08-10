class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n=len(strs)
        minlen=min(len(strs[0]),len(strs[n-1]))
        p=""
        for i in range(minlen):
            if strs[0][i]==strs[n-1][i]:
                p=p+strs[0][i]
            else:
                break
        return p