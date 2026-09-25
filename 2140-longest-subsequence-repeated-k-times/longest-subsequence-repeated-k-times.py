class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans=[]
        temp=[]
        p=len(s)
        x=p//k
        set1={}
        for i in s:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for ch,val in set1.items():
            if val>=k:
                d=ch*(val//k)
                temp.append(d)
        key="".join(temp)
        used={}
        for m in key:
            if m in used:
                used[m]+=1
            else:
                used[m]=1
        next_pos = [[-1] * 26 for _ in range(len(s) + 1)]

        for i in range(len(s) - 1, -1, -1):
            next_pos[i] = next_pos[i + 1].copy()
            next_pos[i][ord(s[i]) - ord('a')] = i

        def isvalid(curr):
            z = curr * k
            pos = 0

            for ch in z:
                if pos >= len(s):
                    return False

                pos = next_pos[pos][ord(ch) - ord('a')]

                if pos == -1:
                    return False

                pos += 1

            return True
        new=[]
        
        def found(key):
            nonlocal new
            nonlocal used
            nonlocal x
            nonlocal ans
            if len(new)>x:
                return
            
            if len(new) > 0 and len(new) >= len(ans):
                if isvalid(new):
                    if len(new) > len(ans) or (len(new) == len(ans) and new > ans):
                        ans = new.copy()
            chars = list(used.keys())
            for ch in chars:
                if used[ch]==0:
                    continue
                new.append(ch)
                used[ch]-=1
                
                found(key)
                used[ch]+=1
                new.pop()
            
        found(key)
        
        return "".join(ans)





