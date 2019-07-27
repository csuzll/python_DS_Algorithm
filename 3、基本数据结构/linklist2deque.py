# 用链表实现双端队列

from unorderlist2 import UnorderedList

class Deque:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.size() == 0

    def size(self):
        return self.size()

    def addFront(self, item):
        self.items.add(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self, item):
        return self.items.pop()

    def remoeRear(self, item):
        return self.items.pop(self.items.size() - 1)