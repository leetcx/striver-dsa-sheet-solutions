class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        m=len(arr)
        n=len(arr[0])
        
        ans = []
        cs=0
        rs=0
        ce=n-1
        re=m-1
        while cs<=ce and rs<=re:

            for i in range(cs,ce+1):
                ans.append(arr[rs][i])
            rs+=1
            for i in range(rs,re+1):
                ans.append(arr[i][ce])
            ce-=1
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    ans.append(arr[re][i])
                re-=1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    ans.append(arr[i][cs])
                cs+=1
        return ans
