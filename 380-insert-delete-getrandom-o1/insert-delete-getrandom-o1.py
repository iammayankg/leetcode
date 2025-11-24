class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        currPos = self.hash[val]
        replacePos = len(self.arr)-1
        self.arr[currPos] = self.arr[replacePos]
        self.hash[self.arr[replacePos]] = currPos
        del self.hash[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.arr)-1)
        return self.arr[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()