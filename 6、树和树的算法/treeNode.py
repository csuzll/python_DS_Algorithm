# 结点类
class TreeNode:
    """ A node for the Binary Search Tree
    可以构造多种类型的结点
    left=None,right=None,parent=None: 创建一个没有左右孩子也没有父结点的结点
    left=lc,right=rc,parent=None: 创建一个有左右孩子但没有父结点的结点
    left=lc,right=None,parent=None: 创建一个有左孩子但没有父结点的结点
    left=None,right=rc,parent=None: 创建一个有右孩子但没有父结点的结点

    left=None,right=None,parent=p: 创建没有左右孩子但有父结点的结点
    left=lc,right=rc,parent=p: 创建一个有左右孩子且有父结点的结点
    left=lc,right=None,parent=p: 创建一个有左孩子且有父结点的结点
    left=None,right=rc,parent=p: 创建一个有右孩子且有父结点的结点
    """
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key # 键
        self.payload = val # 值
        self.leftChild = left # 左孩子或前驱
        self.rightChild = right # 右孩子或后继
        self.parent = parent # 双亲

    # 返回左孩子，可用于判断一个结点是否有左孩子
    def hasLeftChild(self):
        return self.leftChild

    # 返回右孩子，可用于判断一个结点是否有右孩子
    def hasRightChild(self):
        return self.rightChild

    # 判断结点是否是其父结点的左孩子
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    # 判断结点是否是其父结点的右孩子
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # 判断是否是树根（树根的父结点为空）
    def isRoot(self):
        return not self.parent

    # 判断结点是否是叶子结点
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    # 判断是否结点只有一个孩子
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    # 判断结点是否有两个孩子
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    # 替换结点数据
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc

        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    # 在字典(结点类)中实现中序遍历，而不在树中。利用内置函数和yield函数(生成器)
    # __iter__覆盖for x in 操作，此程序是递归的。在TreeNode实例上递归
    def __iter__(self):
        if self:
            if self.hasLeftChild(): # 左孩子
                for elem in self.leftChild: # 调用self.leftChiLd.__iter__()，所以此处是递归的
                    yield elem
            yield self.key # 中
            if self.hasRightChild(): # 右孩子
                for elem in self.rightChild: # 调用self.rightChiLd.__iter__()
                    yield elem

    # 子树中的最小键(任何二叉查找树中的最小值键是树的最左子结点。)
    def findMin(self):
        current = self
        # 通过简单地循环树中每个节点的左子结点，直到它到达没有左子结点的结点
        while current.hasLeftChild():
            current = current.leftChild
        return current

    # 子树中的最大键(任何二叉查找树中的最大值键是树的最右子结点。)
    def findMax(self):
        current = self
        # 通过简单地循环树中每个节点的右子结点，直到它到达没有右子结点的结点
        while current.hasRightChild():
            current = current.rightChild
        return current

    # 求当前结点的中序后继结点
    def findSuccessor(self):
        succ = None
        if self.hasRightChild(): # 结点有右子结点
            # 后继结点为当前结点的右子树中的最小值
            succ = self.rightChild.findMin()
        else: # 没有右子结点
            if self.parent:
                if self.isLeftChild(): # 当前结点是父结点的左子结点
                    # 后继结点为当前结点的父结点
                    succ = self.parent
                else: # 当前结点是父结点的右子结点
                    # 后继结点为此结点的父结点的后继结点(不包括此结点为根的子树)
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    # 求当前结点的中序前驱结点
    def findPredecessor(self):
        prec = None
        if self.hasLeftChild(): # 结点有左子结点
            # 前驱结点为当前结点的左子树中的最大值
            prec = self.leftChild.findMax() 
        else: # 没有左子结点
            if self.parent:
                if self.isRightChild(): # 当前结点是父结点的右子结点
                    # 前驱结点为当前结点的父结点
                    prec = self.parent
                else: # 当前结点是父结点的左子结点
                    # 前驱结点为此结点的父结点的前驱结点(不包括此结点为根的子树)
                    self.parent.leftChild = None
                    prec = self.parent.findPredecessor()
                    self.parent.leftChild = self
        return prec

    # 删除后继结点
    def spliceOut(self):
        if self.isLeaf(): # 如果后继结点是叶子结点
            if self.isLeftChild(): # 左叶子结点
                self.parent.leftChild = None
            else: # 右叶子结点
                self.parent.rightChild = None
        elif self.hasAnyChildren(): # 后继结点有一个子结点
            if self.hasLeftChild(): # 后继结点有左子结点
                if self.isLeftChild(): # 后继结点为其父结点的左子结点
                    self.parent.leftChild = self.leftChild
                else: # 后继结点为其父结点的右子结点
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else: # 后继结点有右子结点
                if self.isLeftChild(): # 后继结点为其父结点的左子结点
                    self.parent.leftChild = self.rightChild
                else: # 后继结点为其父结点的右子结点
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent