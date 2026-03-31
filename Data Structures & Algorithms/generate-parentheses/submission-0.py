class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(Open, Closed):
            if Open == Closed == n:
                res.append("".join(stack))
                return
            
            if Open < n:
                stack.append("(")
                backtrack(Open + 1, Closed)
                stack.pop()
            
            if Closed < Open:
                stack.append(")")
                backtrack(Open, Closed + 1)
                stack.pop()
            
        backtrack(0,0)

        return res