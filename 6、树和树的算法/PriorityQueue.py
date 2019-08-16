# 实现优先队列(最小堆实现)
import unittest

class PriorityQueue:
    """
    实现优先队列为一个二叉堆使用键值对(priority, value)，假设priority是可比的。
    """
    def __init__(self, capacity):
        self.capacity = capacity # 队列除第0位外的容量
        self.priorqueue = [(0,0)] # (0,0)占用0位，不作任何作用
        self.currentSize = 0 # 队列除第0位以外的元素总数

    # 从列表构建优先队列
    def buildHeap(self, alist):
        if len(alist) > self.capacity:
            raise ValueError("列表大小超过队列容量",self.capacity)
        self.currentSize = len(alist)
        self.priorqueue = [(0,0)] + alist[:]
        # 最后一个非叶子结点的索引
        i = self.currentSize // 2
        while i > 0:
            self.perDown(i)
            i -= 1

    # 从位置i处向下调整
    def perDown(self, i):
        while (i * 2) <= self.currentSize: # 子结点存在
            minc = self.minChild(i)
            if self.priorqueue[i][0] > self.priorqueue[minc][0]:
                self.priorqueue[i], self.priorqueue[minc] = self.priorqueue[minc], self.priorqueue[i]
            i = minc

    # 返回位置i的最小子结点的位置(2*i 或 2*i+1)
    def minChild(self, i):
        if i * 2 > self.currentSize: # 说明i位置的是叶子结点
            return -1
        else:
            if i * 2 + 1 > self.currentSize: # 只存在左子结点
                return i * 2
            else:
                # 左右子结点都存在
                if self.priorqueue[i * 2] < self.priorqueue[i * 2 + 1]: # 左结点小于右节点
                    return i * 2
                else: # 右结点小于左结点
                    return i * 2 + 1

    # 从位置i向上调整
    def perUp(self, i):
        while i // 2 > 0:
            if self.priorqueue[i][0] < self.priorqueue[i//2][0]:
                self.priorqueue[i], self.priorqueue[i//2] = self.priorqueue[i//2], self.priorqueue[i]
            i = i // 2

    # 添加元素到队尾
    def enqueue(self, key_value):
        if self.currentSize >= self.capacity:
            self.dequeue()
        self.priorqueue.append(key_value)
        self.currentSize += 1
        self.perUp(self.currentSize)

    # 删除队首元素
    def dequeue(self):
        retVal = self.priorqueue[1][1] 

        self.priorqueue[1] = self.priorqueue[self.currentSize]
        self.currentSize -= 1
        self.priorqueue.pop()
        self.perDown(1)
        return retVal

    # 判空
    def isEmpyt(self):
        if self.currentSize == 0:
            return True
        else:
            return False
    # 实现for... in...
    def __contain__(self, vtx):
        for pair in self.priorqueue:
            if pair[1] == vtx:
                return True
        return False

    # 改变队列中某个元素的优先权的函数并保持队列属性
    def decreaseKey(self, val, newprior):
        """
        val: 值
        newprior: 新优先权
        """
        done = False
        i = 1 # 索引
        myKey = 0 # val在队列中的索引，初始化为0
        # 寻找val在队列中的索引
        while not done and i <= self.currentSize:
            if self.priorqueue[i][1] == val:
                done = True
                myKey = i
            else:
                i += 1
        if myKey > 0: # 找到val在队列中的索引
            # 将新的优先权赋给当前位置的元素
            self.priorqueue[myKey] = (newprior, self.priorqueue[myKey][1])
            # 优先权改变，则需要调整
            self.perUp(myKey)


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.theQueue = PriorityQueue(100)
        self.theQueue.enqueue((2, "x"))
        self.theQueue.enqueue((3, "y"))
        self.theQueue.enqueue((5, "z"))
        self.theQueue.enqueue((6, "a"))
        self.theQueue.enqueue((4, "d"))s

    def testEnqueue(self):
        assert self.theQueue.currentSize == 5

    def testDequeue(self):
        assert self.theQueue.dequeue() == "x"
        assert self.theQueue.dequeue() == "y"

    def testDecKey(self):
        self.theQueue.decreaseKey("d", 1)
        assert self.theQueue.dequeue() == "d"

if __name__ == '__main__':
    unittest.main()