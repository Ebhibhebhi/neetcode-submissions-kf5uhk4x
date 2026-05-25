class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()

        res = 0

        l = 0

        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            res = max(res, len(curr))

        return res







        