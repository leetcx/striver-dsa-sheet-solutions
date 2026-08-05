class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=[0]* n
        rightmax=[0]*n
        leftmax[0]=height[0]
        rightmax[n-1]=height[n-1]
        
        s=0

        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i])
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        for i in range(len(leftmax)):
            s=s+min(leftmax[i],rightmax[i])-height[i]
        return s