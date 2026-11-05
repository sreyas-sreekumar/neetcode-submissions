class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        pile = []
        best = 0

        for i,h in enumerate(heights):
            start = i #default start is its own column
            while pile and pile[-1][1] > h:#top is taller thanh
                s,height = pile.pop()#pop it
                best = max(best,height * (i - s))#for area right edge is i
                start = s #new bar inherits popped start
            pile.append((start,h)) #after clearing out all the taller bars and getting a new best only then do we push. pop everything taller then place yourself with the start inherited
        n = len(heights)

        for s,height in pile:#leftovers
            best = max(best,height * (n - s)) #right edge is n
        return best
