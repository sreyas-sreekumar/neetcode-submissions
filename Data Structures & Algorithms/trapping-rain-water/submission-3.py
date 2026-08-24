class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        curMax = 0
        prefix = []
        suffix = [0] * len(height)
        for i in range(len(height)):
            curMax = max(curMax,height[i])
            prefix.append(curMax)
        curMax = 0
        for i in range(len(height)-1,-1,-1):
            curMax = max(curMax,height[i])
            suffix[i] = curMax
        
        for i in range(len(height)):
            total+= min(suffix[i],prefix[i]) - height[i]
        return total
