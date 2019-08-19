# python创建有序链表

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return self.getData()

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class OrderedList:
    # 初始化，头结点为空
    def __init__(self):
        self.head = None

    # 判空,O(1)
    def isEmpty(self):
        return self.head == None
    
    # 获取链表长度,O(n)
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    # 增加结点，需要在现有的有序列表中查找新项所属的特定位置。最坏O(n)
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        # 寻找新结点的位置
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        # 根据位置（开始或者中间）添加
        temp = Node(item)
        if previous == None: # 插入在头结点位置
            temp.setNext(self.head)
            self.head = temp
        else: # 插入在中间或者尾部
            temp.setNext(current)
            previous.setNext(temp)

    # 删除结点,最坏O(n)
    def remove(self, item):
        current = self.head # 头结点
        previous = None
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()
        if found:
            if previous == None: # 删除头结点
                self.head = current.getNext()
            else: # 删除中间或尾部的结点
                previous.setNext(current.getNext())
        else:
            print("Not found!")

    # 查询是否存在某个结点,最坏O(n)
    def search(self, item):
        current = self.head # 从头结点开始查询
        found = False # 是否找到
        stop = False # 是否停止。如果大于查找值，则停止查找

        while current != None and not found and not stop:
            if current.getData() == item:  # 查找到，True
                found = True
            else:
                # 过了需要查询的值
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()  # 查询下一个节点
        return found 

    def pop(self, pos=0):
        # 判断pos是否越界
        if pos > self.size() - 1 or pos < 0:
            print("pos is not ture!")
            return 

        current = self.head
        previous = None

        # pos为0
        if pos == 0:
            self.head = current.getNext()
            return current.getData()

        # pos非0
        cur_ind = 0
        while cur_ind < pos:
            previous = current
            current = current.getNext()
            cur_ind += 1
        previous.setNext(current.getNext())
        return current.getData()

    # index()查找item是否在链表中，并返回其下标
    def index(self, item):
        current = self.head
        cur_ind = 0
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
                    cur_ind += 1
        if found:
            return cur_ind
        else:
            return -1
if __name__ == '__main__':
    # 测试
    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
