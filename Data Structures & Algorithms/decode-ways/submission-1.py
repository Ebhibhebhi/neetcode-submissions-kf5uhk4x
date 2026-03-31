class Solution:
    def numDecodings(self, s: str) -> int:
        
        a = 0
        b = 1

        for i in range(len(s)-1, -1, -1):
            isvalid1 = 1
            isvalid2 = 1

            if int(s[i]) == 0:
                isvalid1 = 0
                isvalid2 = 0
            elif i == len(s)-1 or int(s[i:i+2]) > 26:
                isvalid2 = 0
            
            tmp = (isvalid1*b) + (isvalid2*a)
            a = b
            b = tmp
        
        return b




