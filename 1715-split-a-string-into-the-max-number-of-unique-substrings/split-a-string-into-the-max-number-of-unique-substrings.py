class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxlen = float('-inf')
        ans = 0
        temp = []

        def maxi(s):
            nonlocal ans
            nonlocal maxlen
            if len(temp) + len(s) <= maxlen:
                return
            if len(s) == 0:
                if len(temp) > maxlen:
                    ans = len(temp)
                    
                    maxlen = len(temp)
                return

            for i in range(len(s)):
                p = s[0:i+1]
                substr = s[i+1:len(s)]

                if p in temp:
                    continue

                temp.append(p)
                maxi(substr)
                temp.pop()

        maxi(s)
        return ans
            
