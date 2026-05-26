class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        my_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for c in s:

            if c in my_map:
                stack.append(c)
            elif len(stack) > 0 and stack[-1] in my_map and c == my_map[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0