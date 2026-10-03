class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def hasduplicate(temp,s2):
            dict1={}
            s1="".join(temp)
            for i in s1:
                dict1[i]=1
            for j in s2:
                if j in dict1:
                    return False
                dict1[j]=1
            return True
                
                    
        memo={}
        def check(i,temp):
          
            if i >= len(arr):
               
                return 0
            state=(i,tuple(temp))
            if state in memo:
                return memo[state]
            oldtemp=temp
            take=0
            if  hasduplicate(temp,arr[i]):
                temp.append(arr[i])
                take=len(arr[i]) + check(i+1,temp)
                temp.pop()
            skip=check(i+1,oldtemp)
            memo[state]=max(take,skip)
            return memo[state]
        return check(0,[])
        

            