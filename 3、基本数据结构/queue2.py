# python实现队列
# 队首在左边（相当于list中index=0的位置），队尾在右边

class Queue:

    def __init__(self):
        self.items = []

    # 判空
    def isEmpty(self):
        return self.items == []

    # 添加新item，
    def enqueue(self, item):
        self.items.append(item)

    # 删除项
    def dequeue(self):
        return self.items.pop(0)

    # 获取队列大小
    def size(self):
        return len(self.items)
        
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.items[1]) 
    q.dequeue()
    print(q.items[0])