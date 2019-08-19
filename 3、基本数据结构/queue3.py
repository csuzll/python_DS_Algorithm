# python实现队列的入队和出队操作为O(1)

# 思路
# 利用两个栈A,B实现。只有特殊情况下B为空时，需要O(n)，其它情况下需要O(1)

from stack import Stack
class Queue:
    """
    入队列：将item加入的inbox中
    出队列：如果outbox为空，将inbox中的item全部pop到outbox中(这一步需要O(n)的操作)，然后将outbox中的top element弹出
    """

    def __init__(self):
        self.inbox = Stack() # 入队的栈
        self.outbox = Stack() # 出队的栈

    # 入队列
    def enqueue(self, item):
        self.inbox.push(item)

    # 出队列
    def dequeue(self):
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()

if __name__ == '__main__':
    q3 = Queue()
    q3.enqueue(1)
    q3.enqueue(2)
    q3.enqueue(3)
    print(q3.dequeue())
    print(q3.dequeue())
    print(q3.dequeue())