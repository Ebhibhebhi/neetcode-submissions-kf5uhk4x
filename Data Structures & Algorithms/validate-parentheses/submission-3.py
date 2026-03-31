class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        myset = {"(", "{", "["}
        stack = []

        myHash = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if s[i] in myset:
                stack.append(s[i])
            elif len(stack) > 0 and myHash[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return False if stack else True