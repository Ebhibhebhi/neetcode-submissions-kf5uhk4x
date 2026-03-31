class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for i in range(len(strs)):

            count = [0] * 26

            for c in strs[i]:
                count[ord(c)-ord('a')]+=1
            
            hashmap[tuple(count)] = [strs[i]] + hashmap.get(tuple(count), [])
        
        res = []

        for v in hashmap.values():
            tmp = []
            for el in v:
                tmp.append(el)
            
            if tmp:
                res.append(tmp)
        
        return res


        
        
        


