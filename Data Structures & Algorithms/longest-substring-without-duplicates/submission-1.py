class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        length = 0
        maxlength = 0
        prev = 0
        for i in range(len(s)):
            while s[i]  in visited:
                visited.remove(s[prev]) 
                prev += 1
            visited.add(s[i])
            length = i - prev + 1
            maxlength = max(maxlength,length)
        return maxlength
        
                
