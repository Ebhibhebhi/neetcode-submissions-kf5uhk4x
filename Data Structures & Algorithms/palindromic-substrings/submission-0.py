class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        mp = 0
        k = 0

        while mp < len(s):
            l = mp
            r = mp + k

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l-=1
                r+=1
            
            if k == 0 and mp + 1 < len(s) and s[mp] == s[mp+1]:
                k = 1
            else:
                mp+=1
                k = 0
        
        return res
            
