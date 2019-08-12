# 二叉最小堆的实现
# 列表实现。列表的第0位默认为0，从位置1开始为堆的开始。
# 当列表从索引1开始存储元素时，每个节点p的左子树的根节点索引应为（2*p），右子树的根节点索引应为（2*p+1）

class BinMinHeap:
    def __init__(self):
        self.heapList = [0] # 列表堆
        self.currentSize = 0 # 堆长度

    # 返回堆大小
    def size(self):
        return self.currentSize

    # 判断是否为空
    def isEmpty(self):
        return 0 == self.currentSize

    # 向上调整函数(为插入时调用)
    def perUp(self, i): 
        """
        在树中向上遍历一个新项，找到其正确位置，维护堆属性。
        """
        while i // 2 > 0: # 父结点存在
            if self.heapList[i] < self.heapList[i // 2]: # 如果当前节点比父结点更小，则交换
                self.heapList[i], self.heapList[i // 2]= self.heapList[i // 2], self.heapList[i]
            i = i // 2

    # 插入一个项，保持最小堆结构和特性
    def insert(self, k):
        """
        1. 将此项添加到列表树末尾
        2. 新添加的项替换到其在堆中的正确位置
        """
        self.heapList.append[k]
        self.currentSize += 1
        self.perUp(self.currentSize)

    # 向下调整函数(为删除时调用)
    def perDown(self, i):
        """
        在树中向下遍历第i项，找到其正确位置，维护堆属性。
        """
        while (i * 2) <= self.currentSize: # 子结点存在
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    # 返回位置i的最小子结点的位置(2*i 或 2*i+1)
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize: # 只存在左结点
            return i * 2
        else:
            # 左右子结点都存在
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]: # 左结点小于右节点
                return i * 2
            else: # 右结点小于左结点
                return i * 2 + 1

    # 删除最小值，保持最小堆的结构和特性
    def delMin(self):
        """
        1. 交换最后一个项到堆的根位置
        2. 从这个根位置沿着树向下推到其正确位置来恢复堆的特性
        """
        if self.currentSize == 0:
            return None
        else:
            retval = self.heapList[1] # 最小值为堆顶元素
            self.heapList[1] = self.heapList[self.currentSize]  # 最后一个项移动到堆根
            self.heapList.pop()  # 删除最后一个项
            self.currentSize -= 1
            self.perDown(1) # 1代表遍历新的根
            return retval

    # 从一个列表构建二叉最小堆，时间复杂度为: O(N)
    def buildHeap(self, alist):
        i = len(alist) // 2 # 超过中间点的任何结点都是树叶
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        # 从最后一个非叶子结点开始调整列表称为列表堆
        while i > 0:
            self.perDown(i)
            i = i - 1

def main():
    bh = BinMinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())

if __name__ == '__main__':
    main()



# 一点想法: 可以用索引0为存储二叉堆的实际元素个数