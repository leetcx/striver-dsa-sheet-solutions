class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        build=[0] *n
        count=0
        
        def req(requests,i,n,count1):
            nonlocal build
            nonlocal count
            
            if i>=len(requests) :
                if all(x == 0 for x in build):
                    count=max(count,count1)
                return
            
            build[requests[i][0]]+=1
            build[requests[i][1]]+=(-1)
           
            req(requests,i+1,n,count1+1)
            
            build[requests[i][0]]-=1
            build[requests[i][1]]+=1
            req(requests,i+1,n,count1)
        req(requests,0,n,0)
        return count

                