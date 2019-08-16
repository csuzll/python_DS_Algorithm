from binMinHeap import BinMinHeap

# 固定容量的堆，当插入时，堆已满，则删除堆顶再插入。否则，正常插入

class MinHeapFix(BinMinHeap):
    def __init__(self, capacity):
        BinMinHeap.__init__(self)
        self.capacity = capacity # 堆容量

    def insert(self, k):
        if self.currentSize >= self.capacity: # 当前堆大小小于堆容量
            self.delMin() # 删掉最小值
        # 正常插入 
        self.heapList.append(k)
        self.currentSize += 1
        self.perUp(self.currentSize)

    # 从一个列表构建二叉最小堆，时间复杂度为: O(N)
    def buildHeap(self, alist):
        if len(alist) > self.capacity:
            raise ValueError("列表大小超过堆容量", self.capacity)
        i = len(alist) // 2 # 超过中间点的任何结点都是树叶
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        # 从最后一个非叶子结点开始调整列表称为列表堆
        while i > 0:
            self.perDown(i)
            i = i - 1

def main():
    # 假设堆容量为5也即是heapList的容量为6
    mhf = MinHeapFix(5)
    # 插满5个数
    for i in range(1, 6):
        mhf.insert(i)
    print(mhf.currentSize) # 输出 5
    print(mhf.heapList) # 输出[0, 1, 2, 3, 4, 5]

    mhf.insert(6) # 插入第6个数
    print(mhf.currentSize) # 输出 5
    print(mhf.heapList) # 输出[0, 2, 4, 3, 5, 6]

if __name__ == '__main__':
    main()


