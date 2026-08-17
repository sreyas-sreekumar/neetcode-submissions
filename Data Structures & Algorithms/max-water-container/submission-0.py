class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentVol = 0
        maxVol = 0
        l = 0
        r = len(heights)-1

        while l< r:
            currentVol = min(heights[l],heights[r]) * (r - l)
            if min(heights[l],heights[r]) == heights[l] :
                l += 1
            elif min(heights[l],heights[r]) == heights[r]:
                r -= 1
            maxVol = max(currentVol,maxVol)
        return maxVol

