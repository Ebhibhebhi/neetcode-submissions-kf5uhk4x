class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        mymap = {}

        for i in range(len(nums)):
            mymap[nums[i]] = 1 + mymap.get(nums[i], 0)
        
        for i in range(k):
            a = max(mymap, key=mymap.get)
            res.append(a)
            del mymap[a]
        
        return res
            

        