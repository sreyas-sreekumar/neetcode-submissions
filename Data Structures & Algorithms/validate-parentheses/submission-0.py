class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeOpen = {
            "}" : "{",
            ")" : "(",
            "]" :"["
        }

#iterate thru the string
        for i in s:
#check if current bracket is a close bracket(closeOpen has closing brackets as key)
            if i in closeOpen:
#check if stack not empty + the top of stack = matching opening bracket for  current closing bracket i
                if stack and stack[-1] == closeOpen[i]:
                    #if so then pop that opening bracket - that pair is done due to LIFO
                    stack.pop()
                else: 
                    #if not then its not valid string due to incorrect order of brackets - the most recent opening bracket is the first one to close
                    return False
            else:
#if our current char is not a closing bracket then its opening bracket ->append to stack
                stack.append(i)
        if not stack:
            return True
        else : 
            return False
        #return False if stack not empty otherwise true
            
        