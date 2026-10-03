class Solution:
    def maxLength(self, arr: list[str]) -> int:
        temp=[]
        def isunique(p):
            if p=="":
                return 0
           
            dict1={}
            for i in p:
                if i in dict1:
                    return False
                dict1[i]=1
            return True
                
                    
        maxlen=float('-inf')
        ans=0
        def check(i):
            nonlocal ans
            nonlocal temp
            nonlocal maxlen
            if i >= len(arr):
                p="".join(temp)
                if  isunique(p):
                    if len(p)> maxlen:
                        ans=len(p)
                        maxlen=len(p)
                return
            temp.append(arr[i])
            check(i+1)
            temp.pop()
            check(i+1)
        check(0)
        return ans
        

            