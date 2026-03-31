class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr = ""
        i = 0

        while i < len(s):
            if s[i] in curr:
                s = s[s.find(s[i]) + 1:]
                result = max(result, len(curr))
                i, curr = 0, ""
            else:
                curr+=s[i]
                i+=1
        result = max(result, len(curr))

        return result
