class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s1count = {}

        for char in s1:
            s1count[char] = 1 + s1count.get(char, 0)
        
        l, r = 0, len(s1) - 1
        curr = {}
        for i in range(l,r+1):
                curr[s2[i]] = 1 + curr.get(s2[i], 0)
        
        while r < len(s2):
            if curr == s1count:
                return True
            curr[s2[l]]-=1
            if curr[s2[l]] == 0:
                del curr[s2[l]]

            l+=1
            r+=1
            if r < len(s2):
                curr[s2[r]] = 1 + curr.get(s2[r], 0)
        
        return False