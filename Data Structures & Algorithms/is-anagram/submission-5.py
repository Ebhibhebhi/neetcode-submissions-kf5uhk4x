class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map1 = {}
        my_map2 = {}

        for i in range(26):
            my_map1[i] = 0
            my_map2[i] = 0
        
        for c in s:
            my_map1[ord(c) - ord('a')] += 1

        for c in t:
            my_map2[ord(c) - ord('a')] += 1

        return my_map1 == my_map2



