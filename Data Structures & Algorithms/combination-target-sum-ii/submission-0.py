class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        
        def dfs(curr, i, total):
            if total == target and curr not in res:
                res.append(curr.copy())
                return

            if total > target or i > (len(candidates)-1):
                return
            
            curr.append(candidates[i])
            dfs(curr, i + 1, total + candidates[i])
            curr.pop()
            dfs(curr, i + 1, total)

        dfs([], 0, 0)

        return res