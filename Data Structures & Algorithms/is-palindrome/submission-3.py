class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "abcdefghijklmnopqrstuvwxyz0123456789"
        caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        tmp = ""
        s1 = set()
        s2 = set()
        
        for c in alphanum:
            s1.add(c)
        
        for c in caps:
            s2.add(c)

        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i] in s2:
                tmp += alphanum[ord(s[i]) - ord('A')]
            elif s[i] in s1:
                tmp += s[i]
            
        l, r = 0, len(tmp) - 1

        while l < r:
            if tmp[l] == tmp[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        




        
            
            

            
