class TimeMap:

    def __init__(self):
        self.parent = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.parent.setdefault(key, {})[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.parent:
            return ""
        
        if timestamp < next(iter(self.parent[key])):
            return ""

        arr = list(self.parent[key].keys())
        l, r = 0, len(arr) - 1
        mid = -1
        while l <= r:
            mid = (l + r)//2

            if mid < len(arr) - 1:
                if arr[mid] <= timestamp < arr[mid + 1]:
                    return self.parent[key][arr[mid]]
            elif mid == len(arr) - 1:
                if arr[mid] <= timestamp:
                    return self.parent[key][arr[mid]]


            if arr[mid] > timestamp:
                r = mid - 1
            
            else: 
                l = mid + 1
            
        #return self.parent[key][arr[mid]]
        
