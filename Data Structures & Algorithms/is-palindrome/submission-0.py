class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanums = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        my_set = set(alphanums)
        pal = ""

        for letter in s:
            if letter in my_set:
                pal += letter
        
        pal = pal.lower()

        for i in range(len(pal)//2):
            if pal[i] != pal[len(pal) - 1 - i]:
                return False
        
        return True