class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours(hour : int):
            return sum(math.ceil(pile/hour) for pile in piles)
        
        low,high = 1, max(piles)
        best = 0
        while low<= high:
            mid = (low+high) // 2
            if hours(mid) <= h :
                best = mid
                high = mid -1 
            else:
                low = mid + 1
        return best