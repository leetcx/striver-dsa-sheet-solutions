class Solution:
    def merge(self, inter: List[List[int]]) -> List[List[int]]:
        inter.sort(key=lambda x:x[0])
        ans=[]
        ans.append(inter[0])
        n= len(inter)
        
        for i in range(1,n):
            if ans[-1][1]>=inter[i][0]:
                ans[-1][1]=max(ans[-1][1],inter[i][1])
            
            else:
                ans.append(inter[i])
        return ans
            

        
          