# python实现无序链表1

class Node:
    # 初始化结点，此时的引用为空
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

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

# 实现无序链表类
class UnorderedList:
    # 初始化，头节点为空
    def __init__(self):
        self.head = None # 头结点
        self.tail = None # 尾结点

    # 检查链表头是否是None的引用，O(1)
    def isEmpty():
        return self.head == None

    # 添加新结点到链表头部，因为这是最简单的添加。O(1)
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail == None:
            # self.tail保持了对最开始进入的结点的引用
            self.tail = temp
        self.head = temp

    # 获取链表的长度，O(n)
    def size(self):
        current = self.head # 从头结点开始计数
        count = 0
        while current!= None:
            count += 1
            current = current.getNext()

        return count

    # 查找item是否在链表中，O(n)
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

        # 查找要删除的结点（有问题，如果遍历完都没有，就会出错。在后续改）
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 如果查找到了，根据查找的位置进行删除
        if previous == None:
            # 即删除链表中的第一个结点
            self.head = current.getNext()
        else:
            # 删除中间或尾部的结点
            # previous指向的结点 指向 current指向的结点的指向结点
            previous.setNext(current.getNext())

    # 添加结点到尾部
    def append(self, item):
        temp = Node(item)
        if self.tail == None: # 没有任何结点
            self.tail = temp
        else: 
            # 有结点
            current = self.tail
            # 从原来的尾结点指向新的结点
            current.setNext(temp)
            # 尾结点更新为最新加入的结点
            self.tail = temp
        # 没有任何结点
        if self.head == None:
            self.head = temp

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


if __name__ == '__main__':
    # 测试
    assert Node(93).getData() == 93, "error"

    # 测试
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))

    mylist.append(123)
    print(mylist.size())