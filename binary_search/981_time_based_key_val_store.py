'''
https://leetcode.com/problems/time-based-key-value-store/description/
'''

class TimeMap:

    def __init__(self):
        self.stamps = dict()
        self.search_space = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.stamps.keys():
            self.stamps[key] += [[value, timestamp]]
            self.search_space[key] += [timestamp]
        else:
            self.stamps[key] = [[value, timestamp]]
            self.search_space[key] = [timestamp]


        return None
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stamps.keys():
            return ""
        search_space_now = self.search_space[key]
        if timestamp < search_space_now[0]:
            return ""
        l, r = 0, len(search_space_now) - 1
        m = (l + r) // 2
        while l <= r:
            if search_space_now[m] == timestamp:
                return self.stamps[key][m][0]
            elif search_space_now[m] < timestamp:
                l = m + 1
                m = (l + r) // 2
            else:
                r = m - 1
                m = (l + r) // 2
        return self.stamps[key][m][0]

def main():
    tm = TimeMap()

     # case 1
    # print(tm.set("foo", "bar", 1))
    # print(tm.get("foo", 1))
    # print(tm.get("foo", 3))
    # print(tm.set("foo", "bar2", 4))
    # print(tm.get("foo", 4))
    # print(tm.get("foo", 5))

    # case 2
    print(tm.set("love","high",10))
    print(tm.set("love","low",20))
    print(tm.get("love",5))
    print(tm.get("love",10))
    print(tm.get("love",15))
    print(tm.get("love",20))
    print(tm.get("love",25))
    return None

if __name__ == "__main__":
    main()
