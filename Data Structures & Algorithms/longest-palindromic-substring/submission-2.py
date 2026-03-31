class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        mp = 0
        k = 0
        while mp < len(s):
            l = mp - 1
            r = mp + 1 + k
            tmp = s[mp] if k == 0 else s[mp:mp+2]
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                tmp = s[l] + tmp + s[l]
                l-=1
                r+=1
            
            if len(tmp) > len(res):
                res = tmp
            
            if k == 0 and mp < len(s) - 1 and s[mp+1] == s[mp]:
                k = 1
            else:
                mp+=1
                k = 0
            
        return res
