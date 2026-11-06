class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        need ={}
        have ={}
        for char in s1:
            need[char] = need.get(char,0) + 1

        length = len(s1)

        for char in s2[:length]:
            have[char] = have.get(char,0) + 1
        
        if have == need:
            return True

        for r in range(length,len(s2)):
            have[s2[r]] = have.get(s2[r],0) + 1
            out = s2[r-length]
            have[out] -=1
            if have[out] == 0:
                del have[out]
            if have == need:
                return True
        return False

        

 

        