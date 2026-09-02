class Solution:
    def intervalIntersection(self, fir: List[List[int]], sec: List[List[int]]) -> List[List[int]]:

        l=0
        h=0
        p=len(fir)
        c=len(sec)
        ans=[]
        while l<p and h<c:
            start=max((fir[l][0]),sec[h][0])
            end=min((fir[l][1]),sec[h][1])
            if start<=end:
                ans.append((start,end))
                if ans[-1][1]<sec[h][1]:
                    l+=1
                else:
                    h+=1
            else:
                if fir[l][1]>=sec[h][1]:
                    h+=1
                else:
                    l+=1
        return ans

