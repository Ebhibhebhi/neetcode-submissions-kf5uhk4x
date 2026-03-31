class Solution:

    def encode(self, strs: List[str]) -> str:
        N = len(strs)
        res = str(N) + "-"
        for i in range(N):
            res += str(len(strs[i])) + "-"
        
        res += "".join(strs)

        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        while s[i]!= "-":
            i+=1
        N = int(s[:i])
        s = s[i+1:]
        
        sizes = []

        for _ in range(N):
            i = 0
            while s[i]!= "-":
                i+=1
            num = int(s[:i])
            s = s[i+1:]

            sizes.append(num)

        res = []
        
        for a in range(N):
            res.append(s[:sizes[a]])
            s = s[sizes[a]:]
        
        return res








        
