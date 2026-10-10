class Solution:
    def longestSubsequence(self, arr: list[int], diff: int) -> int:
        dict1={}
        res=float('-inf')
        for i in range(len(arr)):
            prev=arr[i]-diff
            if prev in dict1:
                dict1[arr[i]]=dict1[prev]+1
            else:
                dict1[arr[i]]=1
            res=max(res,dict1[arr[i]])
            
        return res