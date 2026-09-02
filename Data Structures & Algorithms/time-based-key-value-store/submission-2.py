class TimeMap:

    def __init__(self):
        self.store = {} #key:[[val, timestamp],[val, timestamp]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.store.get(key, [])
        
        #Binary Search
        l,r = 0,  len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1

        return res