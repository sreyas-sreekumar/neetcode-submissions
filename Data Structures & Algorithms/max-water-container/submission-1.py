class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = []
        maxArea = 0 
        left = 0
        right = len(heights)-1
        while left < right:             
            area = min(heights[left],heights[right]) * (right - left)
            maxArea = max(area,maxArea)
            if min(heights[left],heights[right]) == heights[left]:
                left += 1
            else:
                right -=1
             
        return maxArea
            