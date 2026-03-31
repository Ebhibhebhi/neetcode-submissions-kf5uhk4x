class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nested_dict = {i: {} for i in range(len(strs))}
        for i in range(len(strs)):
            for a in range(len(strs[i])):
                if strs[i][a] in nested_dict[i]:
                    nested_dict[i][strs[i][a]] += 1
                else:
                    nested_dict[i][strs[i][a]] = 1
        final_list = []
        used = set()
        for a in range(len(strs)):
            if a in used:
                continue
            sublist = [strs[a]]
            for i in range(a+1, len(strs)):
                if i in used:
                    continue
                elif nested_dict[a] == nested_dict[i]:
                    sublist.append(strs[i])
                    used.add(i)
            final_list.append(sublist)

        return final_list