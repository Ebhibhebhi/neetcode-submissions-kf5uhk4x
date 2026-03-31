class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr = set()
        i = 0

        while i < len(s):
            if s[i] in curr:
                s = s[s.find(s[i]) + 1:]
                result = max(result, len(curr))
                i = 0
                curr.clear()
            else:
                curr.add(s[i])
                i+=1
        result = max(result, len(curr))

        return result
