# python实现双端队列

class Deque:
    def __init__(self):
        self.items = []

    # 判断是否为空
    def isEmpty(self):
        return self.items == []

    # 在首部添加项
    def addFront(self, item):
        self.items.append(item)

    # 在尾部添加项
    def addRear(self, item):
        self.items.insert(0, item)

    # 从首部删除项
    def removeFront(self):
        return self.items.pop()

    # 从尾部删除项
    def removeRear(self):
        return self.items.pop(0)

    # 获取大小
    def size(self):
        return len(self.items)

# d = Deque()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(True)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.removeRear())
# print(d.removeFront())