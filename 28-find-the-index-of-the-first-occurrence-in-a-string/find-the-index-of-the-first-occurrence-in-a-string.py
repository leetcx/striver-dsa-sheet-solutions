class Solution:
    def strStr(self, ha: str, ne: str) -> int:
        n=len(ne)
        p=len(ha)

        for i in range(p):
            if ha[i:i+n]==ne:
                return i
            
        return -1