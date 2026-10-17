class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""
        for c in s:
            if c != " " and c.isalnum() :
                clean += c.lower()
        
        if clean == clean[::-1] :
            return True
        else: 
            return False
        