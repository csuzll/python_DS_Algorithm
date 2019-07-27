# python实现无序链表1

class Node:
    # 初始化结点，此时的引用为空
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return str(self.data)

    # 获取结点中的数据
    def getData(self):
        return self.data

    # 获取对下一个结点的引用
    def getNext(self):
        return self.next

    # 结点重新赋值
    def setData(self, newdata):
        self.data = newdata

    # 结点改变指向
    def setNext(self, newnext):
        self.next = newnext

# 测试
assert Node(93).getData() == 93, "error"


# 实现无序链表类
class UnorderedList:
    # 初始化，头节点为空
    def __init__(self):
        self.head = None # 头结点
        self.tail = None # 尾结点
        self.length = 0 # 存储链表的长度

    def __str__(self):
        datas = []
        current = self.head
        while current:
            datas.append(current.getData())
            current = current.getNext()
        datas = [str(data) for data in datas]
        return "[" + ",".join(datas) + "]"

    # 实现切片操作
    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = list(range(self.size()))[key.start:key.stop:key.step]
            items = []
            for ind in indices:
                items.append(self.__getitem__(ind))
            return items
        elif isinstance(key, int):
            if key < 0:
                key += self.size()
            if key < 0 or key >= self.size():
                raise IndexError("The index (%d) is out of range." % key)
            current = self.head
            cur_ind = 0
            while cur_ind < key:
                current = current.getNext()
                cur_ind += 1
            return current
        else:
            raise TypeError("Invalid argument type.")

    # 检查链表头是否是None的引用，O(1)
    def isEmpty():
        return self.head == None

    # 添加新结点到链表头部，因为这是最简单的添加。O(1)
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail == None:
            # self.tail保持了对最后一个结点的引用
            self.tail = temp
        self.head = temp
        self.length += 1

    # # 获取链表的长度，O(n)
    # def size(self):
    #     current = self.head # 从头结点开始计数
    #     count = 0
    #     while current!= None:
    #         count += 1
    #         current = current.getNext()

    #     return count
    def size(self):
        return self.length

    # 查找item是否在链表中，O(n)，返回Ture或False
    def search(self, item):
        current = self.head # 从头结点开始查询
        found = False
        # 链表没有结束且还没有找到
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    # 删除结点，O(n)
    def remove(self, item):
        current = self.head # current代表要修改的结点。
        previous = None # 要修改的结点的前一个结点
        found = False

        # 查找要删除的结点
        # current不为None保证查找到最后一个结点后完成查找
        # 如果列表为空，此时current=None，则不会进行下面的这个while循环。
        while not found and current:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 如果查找到了，根据查找的位置进行删除
        if found:
            # 链表仅含一个item
            if self.size() == 1:
                self.head = current.getNext()
                self.tail = current.getNext()
                self.length -= 1
            else:
                # 链表大于等于2
                # 删除第一个结点
                if previous == None:
                    self.head = current.getNext()
                # 删除最后一个结点
                elif current.getNext() == None:
                    previous.setNext(current.getNext())
                    self.tail = previous
                else:
                    previous.setNext(current.getNext())
                self.length -= 1
        else:
            print("item not found in the list!")

    # 添加结点到尾部
    def append(self, item):
        temp = Node(item)
        if self.tail == None: # 没有任何结点
            self.tail = temp
        else: 
            # 有结点
            self.tail.setNext(temp)
            # 尾结点更新为最新加入的结点
            self.tail = temp
        # 没有任何结点
        if self.head == None:
            self.head = temp
        self.length += 1

    # # 添加新结点到链表尾部，时间复杂度为O(n)
    # # 当没有尾结点的时候使用
    # def append(self, item):
    #     temp = Node(item)
    #     current = self.head # 从头结点开始查询
    #     previous = None # 记录前一个节点，头结点的前一个节点为None

    #     while current.getNext() != None:
    #         previous = current
    #         current = current.getNext()
    #     previous.setNext(temp) # 修改

    # 返回item在列表中的位置,(元素可重复)
    def index(self, item):
        ind_list = []
        current = self.head
        cur_ind = 0
        while current:
            if current.getData() == item:
                ind_list.append(cur_ind)
            current = current.getNext()
            cur_ind += 1
        return ind_list

    # 删除指定位置的item
    def pop(self, pos=0):
        # 判断pos是否越界,且也包含了空链表情况
        if pos > self.size() - 1 or pos < 0:
            raise Exception("pos is not true!")

        current = self.head
        previous = None

        if self.size() == 1: # 链表只有一个item
            self.head = current.getNext()
            self.tail = current.getNext()
            self.length -= 1
        else: # 链表大于1个item
            if pos == 0: # 0位置需要更新self.head
                self.head = current.getNext()
            else:
                cur_ind = 0
                while cur_ind < pos:
                    previous = current
                    current = current.getNext()
                    cur_ind += 1
                if current.getNext() == None: # 尾结点位置，需要更新self.tail
                    previous.setNext(current.getNext())
                    self.tail = previous
                else: # 其他情况
                    previous.setNext(current.getNext())
            self.length -= 1

        return current.getData()

    # 在指定位置插入item
    def insert(self, pos, item):
        # 判断是否越界
        if pos > self.size() or pos < 0:
            print("pos is not ture!")
            return

        if pos == 0:
            self.add(item)
        elif pos == self.size():
            self.append(item)
        else:
            current = self.head
            previous = None
            cur_ind = 0
            while cur_ind < pos:
                previous = current
                current = current.getNext()
                cur_ind += 1
            temp = Node(item)
            temp.setNext(current)
            previous.setNext(temp)
            self.length += 1


# mylist = UnorderedList()

# mylist.add(31) # 31
# mylist.add(77) # 77,31
# mylist.add(17) # 17,77,31
# mylist.add(93) # 93,17,77,31
# mylist.add(26) # 26,93,17,77,31
# mylist.add(54) # 54,26,93,17,77,31

# print(mylist.size()) # 6
# print(mylist) # 54,26,93,17,77,31
# print(mylist.search(93)) # True
# print(mylist.search(100)) # False

# mylist.add(100) # 100,54,26,93,17,77,31
# print(mylist)
# print(mylist.search(100)) # True
# print(mylist.size()) # 7

# mylist.remove(54) # 100,26,93,17,77,31
# print(mylist.size()) # 6
# mylist.remove(93) # 100,26,17,77,31
# print(mylist.size()) # 5
# mylist.remove(31) # 100,26,17,77
# print(mylist.size()) # 4
# print(mylist.search(93)) # False

# mylist.append(123) # 100,26,17,77,123
# print(mylist) # 100,26,17,77,123
# print(mylist.size()) # 5
# print(mylist.index(3)) # 没有，则返回[]

# for node in mylist[0:3]: # 100,26,17
#     print(node)
# print(mylist[2]) # 17

# print(mylist)
 
# print(mylist.pop(mylist.size()-1)) # 123
# print(mylist.size())
# print(mylist)

# mylist.insert(3, 3) # ,100,26,17,77
# print(mylist)

