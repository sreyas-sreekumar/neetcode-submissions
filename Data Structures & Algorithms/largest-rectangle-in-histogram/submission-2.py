class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        best = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                poppedStart ,poppedHeight = stack.pop()
                best = max(best, poppedHeight * (i - poppedStart))
                start =poppedStart
            stack.append((start,heights[i]))
        
        n = len(heights)
        for i in range(len(stack)):
            poppedStart,poppedHeight = stack.pop()
            best = max(best,poppedHeight * (n - poppedStart))
        return best