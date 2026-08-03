class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # dict with a key and value is a dict

        if key not in self.store:
            self.store[key] = [[timestamp,value]]
        else:
            self.store[key].append([timestamp,value])
        
        

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        if key not in self.store:
            return res
        values = self.store[key]
        l,r = 0, len(values)-1
        while l<=r:
            m = (l+r)//2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m+1
            else:
                r = m-1
        return res

