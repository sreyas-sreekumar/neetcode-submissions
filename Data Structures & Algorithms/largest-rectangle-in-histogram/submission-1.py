class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        best = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                startPopped,heightPopped = stack.pop()
                best = max(best,heightPopped * (i - startPopped))
                start = startPopped
            stack.append((start,heights[i]))
        
        n = len(heights)
        for i in range(len(stack)):
            startPopped,heightPopped = stack.pop()
            best = max(best,heightPopped * (n - startPopped))
        
        return best
                
            