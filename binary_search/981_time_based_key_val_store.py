'''
https://leetcode.com/problems/time-based-key-value-store/description/
'''

class TimeMap:

    def __init__(self):
        self.stamps = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.stamps.keys():
            self.stamps[key] += [[value, timestamp]]
        else:
            self.stamps[key] = [[value, timestamp]]
        return None
    def get(self, key: str, timestamp: int) -> str:
        search_space = [x[1] for x in self.stamps[key]]
        if len(search_space) == 1:
            return self.stamps[key][0][0]
        l, r = 0, len(search_space) - 1
        m = (l + r) // 2
        while l <= r:
            if search_space[m] == timestamp:
                return self.stamps[key][m][0]
            elif search_space[m] < timestamp:
                r = m - 1
                m = (l + r) // 2
            else:
                l = m + 1
                m = (l + r) // 2
        return self.stamps[key][m][0]

def main():
    tm = TimeMap()
    print(tm.set("foo", "bar", 1))
    print(tm.get("foo", 1))
    print(tm.get("foo", 3))
    print(tm.set("foo", "bar2", 4))
    print(tm.get("foo", 4))
    print(tm.get("foo", 5))

    return None

if __name__ == "__main__":
    main()
