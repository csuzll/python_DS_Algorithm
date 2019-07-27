# 用链表实现队列
from unorderlist2 import UnorderedList

class Queue2:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.size() == 0

    def size(self):
        return self.items.size()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self, item):
        self.items.pop()