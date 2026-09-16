class Solution:
    def merge(self, inter: list[list[int]]) -> list[list[int]]:
        ans=[inter[0]]
        inter.sort(key=lambda x:x[0])
        ans[0]=inter[0]
        for i in range(1,len(inter)):
            if ans[-1][1]>= inter[i][0]:
                ans[-1][1]=max(ans[-1][1],inter[i][1])
            else:

                ans.append(inter[i])
        return ans
