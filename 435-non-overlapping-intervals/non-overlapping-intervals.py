class Solution:
    def eraseOverlapIntervals(self, inter: List[List[int]]) -> int:
        inter.sort(key= lambda x:x[0])
        ans=[]
        ans.append(inter[0])
        n=len(inter)
        c=0

        for i in  range (1,n):
            if ans[-1][1] > inter[i][0]:
                c+=1
                ans[-1][1]=min(ans[-1][1],inter[i][1])
            else:
                ans.append(inter[i])
        return c

