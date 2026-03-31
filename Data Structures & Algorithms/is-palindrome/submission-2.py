class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanums = "abcdefghijklmnopqrstuvwxyz"
        alphabet = set()
        for c in alphanums:
            alphabet.add(c)
        
        all_stuff = alphanums + "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        all_letters = set()

        for c in all_stuff:
            all_letters.add(c)
        
        new = []
        for c in s:
            if c not in alphabet:
                if c not in all_letters:
                    continue
                new.append(alphanums[ord(c)-ord("A")])
            else:
                new.append(c)
            
        l, r = 0, len(new) - 1

        while l < r:
            if new[l] != new[r]:
                return False

            l+=1
            r-=1

        return True
            
            

            
