class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i].lower()
        
        if "".join(reversed(string)) == string:
            return True
        else :
            return False


        