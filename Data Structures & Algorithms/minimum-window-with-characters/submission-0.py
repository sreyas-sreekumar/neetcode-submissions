class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have ={}
        required = len(need)
        formed = 0
        l = 0

        best = (float('inf'),0,0)

        for r,c in enumerate(s):
            have[c] = have.get(c,0) +1
            if have[c] == need[c]:
                formed+=1
            
            while formed == required:
                if r-l +1 < best[0]:
                    best = (r-l+1,l,r)
                left = s[l]
                have[left] -=1
                if left in need and have[left] < need[left]:
                    formed -=1
                l +=1
        
        if best[0] == float('inf'):
            return ""
        return s[best[1]:best[2]+1]
