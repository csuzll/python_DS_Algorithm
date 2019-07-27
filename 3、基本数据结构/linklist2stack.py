# 用链表实现栈

from unorderlist2 import UnorderedList

class Stack2():
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.size() == 0

    def size(self):
        return self.items.size()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop(self.items.size() - 1)

    def peek(self):
        self.items[-1]
