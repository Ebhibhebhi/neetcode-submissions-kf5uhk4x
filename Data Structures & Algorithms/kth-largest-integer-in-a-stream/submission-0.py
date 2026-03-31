class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.my_list = sorted(nums)
        self.k = k
    def add(self, val: int) -> int:
        self.my_list.append(val)
        self.my_list.sort()
        return self.my_list[-self.k]
