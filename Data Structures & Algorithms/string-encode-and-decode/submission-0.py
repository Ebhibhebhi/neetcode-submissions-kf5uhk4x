class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = (str(len(strs)) + "-")

        for i in range(len(strs)):
            final_string += (str(len(strs[i])) + '-')
        
        for i in range(len(strs)):
            final_string += strs[i]
        
        return final_string


    def decode(self, s: str) -> List[str]:
        i = 0
        elements = ""

        while s[i] != '-':
            elements += s[i]
            i+=1
        i += 1
        wordsizes = [""] * int(elements)

        for a in range(int(elements)):
            while s[i] != '-':
                wordsizes[a] += s[i]
                i+=1
            i+=1
        
        final_list = []

        for a in range(int(elements)):
            final_list.append(s[i:int(wordsizes[a])+i])
            i += int(wordsizes[a])
        
        return final_list





