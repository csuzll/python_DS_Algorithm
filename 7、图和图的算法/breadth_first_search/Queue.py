# 队列类
# 队首在右边，队尾在左边（相当于list中index=0的位置）

class Queue:

    def __init__(self):
        self.items = []

    # 判空
    def isEmpty(self):
        return self.items == []

    # 添加新item，队尾在list的位置为0，O(n)
    def enqueue(self, item):
        self.items.insert(0, item)

    # 删除项，队首在list的最后一个元素，O(1)
    def dequeue(self):
        return self.items.pop()

    # 获取队列大小
    def size(self):
        return len(self.items)