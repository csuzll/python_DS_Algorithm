"""
题: 实现一个简单的哈希映射。

要求：
put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
remove(key)：如果映射中存在这个键

注意：
所有的值都在 [1, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希库。
"""

# 实现方法一: 利用数组下标和值来表示哈希映射关系
class MyHashMap1:
    # 初始化大小为100001的bitmap，值全为-1
    def __init__(self):
        self.bitmap = [-1] * 1000001

    # 添加
    def put(self, key, value):
        self.bitmap[key] = value

    # 获取
    def get(self, key):
        return self.bitmap[key]

    # 删除
    def remove(self, key):
        self.bitmap[key] = -1

# 实现方法二: 以简单取余法作为哈希函数，链地址法为解决冲突方法，构造哈希表
# 省内存
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000                       # 键值块，哈希桶
        self.itemsPerBuckect = 1001               # 产生冲突的“拉链”块
        self.hashmap = [[] for _ in range(self.buckets)]     

    # 散列函数
    def hash(self, key):
        return key % self.buckets                 # 取余

    # 处理冲突的函数
    def pos(self, key):
        return key // self.buckets                # 向下取整，返回商的整数部分

    def put(self, key, value):
        """
         value will always be positive.
         :type key: int
         :type value: int
         :rtype: void
        """
        hashkey = self.hash(key)   # 哈希值，对应hashmap的索引。
        if not self.hashmap[hashkey]:                 # 没有产生冲突，直接填入buckets中
            self.hashmap[hashkey] = [None] * self.itemsPerBuckect
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        if(not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:      # 没有找到这个值
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None

# 实现方法3
class MyHashMap3(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bitmap = [[-1] * 1000 for _ in range(1001)] # 二维数组，所有值直接为-1

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        row, col = key / 1000, key % 1000 # 行为索引，列的索引位为key，索引位存储的值为数据。
        self.bitmap[row][col] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        row, col = key / 1000, key % 1000
        return self.bitmap[row][col]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        row, col = key / 1000, key % 1000
        self.bitmap[row][col] = -1

if __name__ == '__main__':
    # 测试
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(hashMap.get(1))         # returns 1
    print(hashMap.get(3))         # returns -1 (not found)
    hashMap.put(2, 1)      # update the existing value
    print(hashMap.get(2))         # returns 1 
    hashMap.remove(2)      # remove the mapping for 2
    print(hashMap.get(2))         # returns -1 (not found) 