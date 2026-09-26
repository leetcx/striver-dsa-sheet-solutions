class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        used={1:1}
        for i in range(2,n+1):
            used[i]=2
        temp=[]
        ans=[0] * (2*n-1)
       
        def back(pos):
            nonlocal ans
            nonlocal temp
            nonlocal used
            if pos==(2*n)-1:
               
                
                return True
            if ans[pos] != 0:
                return back(pos+1)
            for i in range(n,0,-1):
                if used[i]==0:
                    continue
                if i==1:
                    ans[pos]=i
                    used[i]-=1
                    if back(pos+1):
                        return True
                    ans[pos]=0
                    used[i]+=1
                else:
                    if pos+i>=(2*n)-1:
                        continue
                    if ans[pos+i] !=0:
                        continue
                    ans[pos]=i
                    ans[pos+i]=i
                    used[i]-=2
                    if back(pos+1):
                        return True
                    ans[pos]=0
                    ans[pos+i]=0
                    used[i]+=2
                

                

                
        back(0)
        
        return ans
        

            
