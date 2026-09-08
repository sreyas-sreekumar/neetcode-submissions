class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        string = ""
        longest = ""
        prev = 0
        for i in range(len(s)):
            while s[i]  in visited:
                visited.remove(s[prev]) 
                string = string[1:]
                prev += 1
            visited.add(s[i])
            string += s[i]
            if len(string) > len(longest):
                longest = string
        return len(longest)
                
