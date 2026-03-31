class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dyct = defaultdict(int)
        result = []

        for i in range(len(nums)):
            if nums[i] in dyct:
                dyct[nums[i]]+=1
            else:
                dyct[nums[i]]=1
        
        for i in range(k):
            max_key = max(dyct, key=dyct.get)
            result.append(max_key)
            del dyct[max_key]

        return result
