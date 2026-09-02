class Solution:
    def trap(self, height: List[int]) -> int:
        p=len(height)
        leftmax=[0] * p
        rightmax=[0] * p
        leftmax[0]=height[0]
        rightmax[-1]=height[-1]
        total=0
        for i in range(1,len(height)):
            leftmax[i]=max(leftmax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        for i in range(len(height)):
            total+=min(leftmax[i],rightmax[i])-height[i]
        return total

        