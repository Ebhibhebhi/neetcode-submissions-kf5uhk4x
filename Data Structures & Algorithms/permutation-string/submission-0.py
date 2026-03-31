class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = {}

        for char in s1:
            s1count[char] = 1 + s1count.get(char, 0)
        
        l, r = 0, len(s1) - 1

        while r < len(s2):
            curr = {}
            for i in range(l,r+1):
                curr[s2[i]] = 1 + curr.get(s2[i], 0)
            if curr == s1count:
                return True
            l+=1
            r+=1
        
        return False