class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        mem = [-1] * len(s)

        def dfs(l):

            if mem[l] != -1:
                return mem[l]

            if s[l:] in words:
                return True

            r = l + 1
            
            while r < len(s):
                if s[l:r] in words:
                    
                    if dfs(r):
                        mem[l] = True
                        return True
                
                r+=1
            
            mem[l] = False

            return False
        
        return dfs(0)
            
            

            