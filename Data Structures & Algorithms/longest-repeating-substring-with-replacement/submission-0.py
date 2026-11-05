class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxF = 0
        best = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxF = max(maxF,count[s[r]]) #why is this not in the while loop -> it only changes when a new letter is added -> updated once per new right char r. shrinking l removes letters ,lowering trueMax
            while ((r - l) + 1) - maxF > k :
                count[s[l]] -=1
                l +=1
            best = max(best,r-l + 1)#why is it not maxD
        return best