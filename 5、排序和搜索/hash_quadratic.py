# hash表构造

# 构造以简单取余法作为哈希函数，二次探测为解决冲突方法，大小为11的哈希表

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.num = 0

    def hashfuction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):