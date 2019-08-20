# hash查找

# 构造以简单取余法作为哈希函数，间隔为1的线性探测为解决冲突方法，大小为11的哈希表
# 当hash表满时，扩充hash表的大小
# 实现哈希表相当于实现一个Map

class HashTable:
    def __init__(self):
        self.size = 11 # 哈希表大小
        self.slots = [None] * self.size  # slots列表，保存key
        self.data = [None] * self.size   # data列表，保存value
        self.load_factor = 0.75  # 装载因子
        self.num = 0  # 装入元素个数

    # 哈希函数: 简答取余法
    def hashfuction(self, key, size):
        return key % size

    # # 字符串的哈希函数，加权方法
    # def string_hashfuction(self, keystr):
    #     hashvalue = 0
    #     for i, c in enumerate(keystr):
    #         hashvalue += (i+1) * ord(c)
    #     print(hashvalue)
    #     hashvalue = hashvalue % self.size
    #     return hashvalue

    # 冲突解决: 间隔为1的线性探测
    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    # # 扩容（不知道实现的对不对）
    # def resize(self):
    #     # 扩容到原有元素数量的两倍
    #     self.size = self.num * 2
    #     tempslots = self.slots[:] # 复制，必须深复制
    #     tempdata = self.data[:] # 复制，必须深复制

    #     # 构建空的新的大小的slots和data列表
    #     self.slots = [None] * self.size  # slots列表，保存key
    #     self.data = [None] * self.size   # data列表，保存value

    #     # 扩容后将原来的key，value放在新的位置
    #     for key, value in zip(tempslots, tempdata):
    #         # 存入原来已有的元素
    #         if key != None:
    #             hashvalue = self.hashfuction(key, self.size) 
    #             if self.slots[hashvalue] == None:
    #                 self.slots[hashvalue] = key
    #                 self.data[hashvalue] = value
    #             else:
    #                 if self.slots[hashvalue] == key:
    #                     self.data[hashvalue] = value
    #                 else:
    #                     newhashvalue = self.rehash(hashvalue, self.size)
    #                     while self.slots[newhashvalue] != None and self.slots[newhashvalue] != key:
    #                         newhashvalue = self.rehash(newhashvalue, self.size)
    #                     if self.slots[newhashvalue] == None:
    #                         self.slots[newhashvalue] = key
    #                         self.data[newhashvalue] = value
    #                     else:
    #                         self.data[newhashvalue] = value # replace

    # 插入key和value
    def put(self, key, value):
        hashvalue = self.hashfuction(key, self.size) # 计算哈希值

        if self.slots[hashvalue] == None: # 哈希值处为空位，则可以放置键值对
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
            self.num += 1
            # # 如果比例大于装载因子
            # if (self.num/len(self.slots) > 0.75):
            #     self.resize()
        else: 
            if self.slots[hashvalue] == key:   # 哈希值处不为空，旧key对与新key值相同，则作为更新，更新value
                self.data[hashvalue] = value  # replace
            else: # 哈希值处不为空，key值也不同，发生冲突，则继续探测
                newhashvalue = self.rehash(hashvalue, self.size)
                while self.slots[newhashvalue] != None and self.slots[newhashvalue] != key:
                    newhashvalue = self.rehash(newhashvalue, self.size)

                if self.slots[newhashvalue] == None:
                    self.slots[newhashvalue] = key
                    self.data[newhashvalue] = value
                    self.num += 1
                    # # 如果比例大于装载因子
                    # if (self.num/len(self.slots) > 0.75):
                    #     self.resize()
                else:
                    self.data[newhashvalue] = value # replace

    # 支持以"HashTable[key]=value"方式添加
    def __setitem__(self, key, value):
        self.put(key, value)

    # 获取value（哈希查找的复杂度并不完全是O(1)，取决于哈希表的负载因子。负载因子越大，发生碰撞的可能性越高）
    def get(self, key):
        startslot = self.hashfuction(key, self.size) # 计算哈希值, 最初的哈希值，作为重新散列探测的停止条件

        data = -1 # -1表示没找到，返回-1
        stop = False
        found = False
        position = startslot  

        # key不为空，且没找到且没停止
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key: # key值与寻找的key值相同，则data赋值为相应的value值
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size) # 重新散列
                # 重新散列回到初始哈希值时，说明无法找到，可以停止了
                if position == startslot:
                    stop = True
        return data

    # 支持以"HashTable[key]"方式读取
    def __getitem__(self, key):
        return self.get(key)

    # # 删除key和value 
    # # (这样删除是有问题的，比如删除记录a，记录b是在a之后插入的且与a有冲突，a的位置变为空槽，这样会导致记录b在a的位置重新插入数据前不可见)
    # def delet(self, key):
    #     startslot = self.hashfuction(key, self.size) # 计算哈希值, 最初的哈希值，作为重新散列探测的停止条件
    #     position = startslot 

    #     if self.slots[position] == None: # 哈希值处为空位，则不存在该键值对，无需删除
    #         return 
    #     elif self.slots[position] == key: # 哈希值处不为空，key值与寻找中的key值相同，则删除
    #         self.slots[position] = None
    #         self.data[position] = None
    #         self.num -= 1
    #         return
    #     else:
    #         position = self.rehash(position, self.size) # 重新散列

    #         while self.slots[position] != None and self.slots[position] != key:
    #             position = self.rehash(position, self.size)
    #             if position == startslot: # 哈希值探测重回起点，判断为无法找到了
    #                 return

    #         # 结束了while循环，意味着找到了空位或相同的key值
    #         if self.slots[position] == None:
    #             return
    #         else:
    #             self.slots[position] = None
    #             self.data[position] = None
    #             self.num -= 1
    #             return

    # # 支持以"del HashTable[key]"方式删除
    # def __delitem__(self, key):
    #     self.delet(key)

    # 实现for key in hashtable
    def __contains__(self, key):
        if self.get(key) != -1:
            return True
        else:
            return False

    # 实现for ... in ...
    # 遍历key
    def __iter__(self):
        for key in self.slots:
            if key != None:
                yield key

    # 支持以"len(HashTable)"获取key的数量
    def __len__(self):
        return self.num

if __name__ == '__main__':
    # 测试
    H = HashTable()

    # 添加
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"

    print(H.slots)
    print(H.data)
    print(len(H))

    print(H[17])
    H[17] = 'duck'
    print(H[17])
    print(H[99]) # 输出-1，因为没有key=99

    # 测试__contains__()方法
    if 77 in H:
        print("77 is in H")

    for k in H:
        print(k, end=" ")