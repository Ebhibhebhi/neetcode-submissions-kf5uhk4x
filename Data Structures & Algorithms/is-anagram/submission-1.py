class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letters_s = {}
        for i in range(len(s)):
            if s[i] in letters_s:
                letters_s[s[i]] += 1
            else:
                letters_s[s[i]] = 1
        
        letters_t = {}
        for i in range(len(t)):
            if t[i] in letters_t:
                letters_t[t[i]] += 1
            else:
                letters_t[t[i]] = 1
        
        return letters_s == letters_t


