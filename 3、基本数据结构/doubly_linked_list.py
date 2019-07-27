# python实现双向链表
# 双向链表就是将链表首尾相接。

class DoublyNode:
    """结点类型"""
    def __init__(self, initdata):
        self.data = initdata # 保存元素
        self.next = None # 保存下一个结点
        self.prev = None # 保存上一个结点

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

    def getPrev(self):
        return self.prev

    def setPrev(self, newprev):
        self.prev = newprev

class DoublyLinkList:
    # 初始化双向链表
    def __init__(self):
        self.head = None # 指定一个head引用头结点
        self.length = 0

    # 判空
    def isEmpty(self):
        return self.length == 0

    # 求链表长度
    def size(self):
        return self.length

    # 遍历链表
    def travel(self):
        # 定义游标
        cur = self.head
        while cur != None:
            print(cur.getData(), end=" ")
            cur = cur.getNext()
        print("")

    # 在链表头部插入元素
    def add(self, item):
        node = DoublyNode(item)
        if self.isEmpty(): # 如果是空列表
            self.head  = node
        else:
            # 将node的next指向head头结点
            node.setNext(self.head)
            # 将头结点的prev指向node
            self.head.setPrev(node)
            # 将head指向node(更新head)
            self.head = node
        self.length += 1

    # 在链表尾部插入元素
    def append(self, item):
        node = DoublyNode(item)
        if self.isEmpty(): # 如果是空链表
            self.head = node
        else:
            # 移动到链表尾部
            cur = self.head
            while cur.getNext() != None:
                cur = cur.getNext()
            # 退出循环后，cur指向的就是最后一个结点。
            # 将尾结点cur的next指向node
            cur.setNext(node)
            # 将node的prev指向cur
            node.setPrev(cur)
        self.length += 1

    # 查找元素是否存在
    def search(self, item):
        cur = self.head
        found  = False

        while cur != None and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
        return found

    # 指定位置插入结点
    def insert(self, pos, item):
        # 判断是否越界
        if pos > self.size() or pos < 0:
            print("pos is not ture!")
            return

        # 在指定位置添加结点
        if pos == 0:
            self.add(item)
        elif pos == self.size():
            self.append(item)
        else:
            node = DoublyNode(item)
            cur = self.head
            cur_ind = 0
            # 移动到指定位置的前一个位置
            while cur_ind < pos - 1:
                cur_ind += 1
                cur = cur.getNext()
            # 将node的prev指向cur
            node.setPrev(cur)
            # 将node的next指向cur的下一个结点
            node.setNext(cur.getNext())
            # 将cur的下一个结点的prev指向node
            cur.getNext().setPrev(node)
            # 将cur的next指向node
            cur.setNext(node)
            self.length += 1

    # 删除元素
    def remove(self, item):
        cur = self.head

        while cur != None:
            # 找到了要删除的元素
            if cur.getData() == item:
                # 先判断是否是头结点
                # 头结点
                if cur == self.head:
                    self.head = cur.getNext()
                    # 如果存在下一个结点，则设置下一个结点
                    if cur.getNext():
                        # 将cur的下一个结点的前向指针设置为None
                        cur.getNext().setPrev(None)
                else:
                    # cur结点的前一个结点设置其next指向cur结点的下一个结点
                    cur.getPrev().setNext(cur.getNext())
                    # 如果存在下一个结点，则设置下一个结点
                    if cur.getNext():
                        # 将cur结点的下一个结点的prev指向cur的前一个结点
                        cur.getNext().setPrev(cur.getPrev())
                self.length -= 1
                break
            else:
                cur = cur.getNext()

# 测试
if __name__=="__main__":
    dll = DoublyLinkList()

    dll.add(1) # [1]
    dll.travel()

    dll.add(2) # [2,1]
    dll.travel()

    dll.append(3)  # [2,1,3]
    dll.travel()

    dll.insert(2, 4) # [2,1,4,3]
    dll.travel()

    dll.insert(4, 2) # [2,1,4,3,2]
    dll.travel() 

    dll.insert(0, 6) # [6,2,1,4,3,2]
    dll.travel()

    print("length: ", dll.size()) # 6

    print(dll.search(3)) # True
    print(dll.search(4)) # True
    print(dll.search(5)) # False

    dll.remove(1) # [6,2,4,3,2]
    print("length: ", dll.size()) # 5
    dll.travel()