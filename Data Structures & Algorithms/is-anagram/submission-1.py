from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        groupS = defaultdict(int)
        groupT = defaultdict(int)
        if len(s) != len(t):
            return False
        for item in range(len(s)):
            char = s[item]
            charTwo = t[item]
            groupS[char]+=1
            groupT[charTwo]+=1
        if groupS == groupT:
            return True
        else:
            return False
        

        