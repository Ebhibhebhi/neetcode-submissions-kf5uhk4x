class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, num_open, num_closed):
            if num_open < num_closed:
                return
            if num_open > n or num_closed > n:
                return
            if len(curr) == 2*n:
                res.append(curr.copy())
                return
            
            curr.append("(")
            dfs(curr, num_open + 1, num_closed)
            curr.pop()
            curr.append(")")
            dfs(curr, num_open, num_closed + 1)
            curr.pop()

        dfs([], 0, 0)
        
        for i in range(len(res)):
            res[i] = "".join(res[i])
        
        return res


            
