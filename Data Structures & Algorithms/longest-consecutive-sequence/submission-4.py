class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            currentNum = num
            currentStreak = 1
            if num - 1 in numSet :
                continue
            while(currentNum + 1 in numSet):
                currentStreak += 1
                currentNum +=1
            longest = max(longest,currentStreak)
        return longest
            
