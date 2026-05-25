class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        my_map = {}

        for i in nums:
            my_map[i] = 1 + my_map.get(i, 0)

        for i in range(k):
            r = max(my_map, key=lambda k: my_map[k])
            res.append(r)
            del my_map[r]
        
        return res

