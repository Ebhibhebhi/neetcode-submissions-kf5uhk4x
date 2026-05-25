class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_map = {}

        for i in range(len(strs)):

            tup = [0] * 26
            word = strs[i]

            for c in word:
                tup[ord(c) - ord('a')] += 1
            
            if tuple(tup) in my_map:
                my_map[tuple(tup)].append(word)
            else:
                my_map[tuple(tup)] = [word]
            
        res = []

        for val in my_map.values():
            res.append(val)

        return res
                
            
            









        
        
        


