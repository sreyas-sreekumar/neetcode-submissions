class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        currentArea = 0
        maxArea = 0

        left = 0 
        right = len(heights) - 1


        while left < right:
            currentArea = min(heights[left],heights[right]) * (right - left)

            maxArea = max(maxArea,currentArea)

            if min(heights[left],heights[right]) == heights[left]:
                left += 1
            else:
                right -=1

        return maxArea