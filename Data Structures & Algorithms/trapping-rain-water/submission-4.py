class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        tallestSoFar = 0
        result = 0

        for i in range(len(height)):
            tallestSoFar = max(tallestSoFar,height[i])
            leftMax[i] = tallestSoFar

        tallestSoFar = 0
        for i in range(len(height)-1,-1,-1):
            tallestSoFar = max(tallestSoFar,height[i])
            rightMax[i] = tallestSoFar

        for i in range(len(height)):
            result += min(leftMax[i],rightMax[i]) - height[i]
        return result


