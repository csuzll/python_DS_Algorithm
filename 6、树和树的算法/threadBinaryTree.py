# 下边实现的是Double Thread。

from treeNode import TreeNode
from binarySearchTree import BinarySearchTree

class DoubleThreadedNode(TreeNode):
    def __init__(self, key, val, left=None, right=None, parent=None):
        TreeNode.__init__(self, key, val, left, right, parent)

        self.ltag = 0 # 左标志，0表示该结点的left指向左孩子，1表示该结点的left指向前驱结点
        self.rtag = 0 # 右标志，0表示该结点的right指向右孩子，1表示该结点的right指向后继结点
        # if self.leftChild != None:
        #     self.ltag = 
        # if self.rightChild != None:
        #     self.rtag = True

class DoubleThreadedBinaryTree(BinarySearchTree):
    # 无初始化
    # 重写一些函数

    # 重写插入数据（线索化之前的插入）
    # 将键值对放入树中，并调整保持二叉查找树属性
    """ put的性能: 取决于树的高度"""
    def put(self, key, val):
        if self.root: 
            # 树有根，调用私有递归辅助函数_put()
            self._put(key, val, self.root)
        else:
            # 没有根，创建一个新的TreeNode作为树的根
            self.root = DoubleThreadedNode(key, val)
            self.size += 1

    # 树有根的情况下的插入函数
    def _put(self, key, val, currentNode):
        if key == currentNode.key: # 新键等于当前结点的键，修改当前结点的payload
            currentNode.replaceNodeData(key, val, currentNode.leftChild, currentNode.rightChild)
        elif key < currentNode.key: # 新键小于当前结点的键，搜索左子树
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                # 当前结点的左结点设置为新建
                currentNode.leftChild = DoubleThreadedNode(key, val, parent=currentNode)
                self.size += 1
        else: # 新键大于当前结点的键，搜索右子树
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                # 当前结点的右结点设置为新键
                currentNode.rightChild = DoubleThreadedNode(key, val, parent=currentNode)
                self.size += 1

    # # 前序遍历线索化
    # def prevThreading(self):
    #     self._prevThreading(self.root)

    # def _prevThreading(self, tree, prev):
    #     """
    #     tree: 表示正在访问的结点
    #     prev: 表示上一个刚刚访问的结点
    #     """
    #     if tree:
    #         if tree.leftChild == None: # 当前结点左孩子不存在
    #             tree.ltag = 1
    #             tree.leftChild = prev
    #         if prev != None and prev.rightChild == None: # 当前结点的前一个结点的右孩子不存在
    #             prev.rtag = 1
    #             prev.rightChild = tree
    #         prev = tree # prev设置为当前结点
    #         if tree.ltag == 0:
    #             self._prevThreading(tree.leftChild, prev)
    #         if tree.rtag == 0:
    #             self._prevThreading(tree.rightChild, prev)

    # # 线索二叉树的前序遍历
    # def prevThreadOrder(self):
    #     self._prevThreadOrder(self.root)

    # def _prevThreadOrder(self, tree, prev=None):
    #     cur = tree
    #     # while cur: #树空或已经到最后一个结点时停止循环
    #     #     while cur.ltag == 0:
    #     #         print(cur.key, end=" ")
    #     #         cur = cur.leftChild
    #     #     print(cur.key, end = " ")
    #     #     cur = cur.rightChild
    #     while cur:
    #         print(cur.key, end=" ") # 打印结点
    #         if cur.ltag == 0: # 当前结点的左孩子存在时，下一个结点为左孩子 
    #             cur = cur.leftChild
    #         else: # 若左孩子不存在，则下一个结点为当前结点的右孩子 
    #             # 若右孩子也不存在，则下一个结点为当前结点的后继 
    #             cur = cur.rightChild

    # 中序线索化二叉搜索树
    def inThreading(self):
        self._inThreading(self.root)

    def _inThreading(self, tree, prev=None):
        """
        tree: 当前正在访问的结点
        prev: 上一次访问的结点
        """
        if tree != None:
            self._inThreading(tree.leftChild, prev)
            if tree.leftChild == None: # 如果当前结点的左孩子不存在，则修改当前结点的标志，并使其左指针指向前一个结点
                tree.ltag = 1
                tree.leftChild = prev # 指向前驱结点
            if prev != None and prev.rightChild == None: # 如果存在前驱结点且前驱结点的右孩子不存在，则修改前驱结点的右标志，并使其右指针指向当前结点
                prev.rtag = 1
                prev.rightChild = tree # 指向后继结点
            prev = tree # 将前一个结点设置为当前结点，为下一轮作准备 
            self._inThreading(tree.rightChild, prev)
        else:
            return None

    # 覆盖掉父类的中序遍历方法
    # 线索二叉树的中序遍历
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tree):
        p = trees
        while p: # 树空或已经到达最后一个结点时停止循环
            # 找到最左的点
            while p.ltag != 1: # 遍历左子树，直到一个没有左孩子的结点
                p = p.leftChild
            print(p.key, end = " ") # 打印该结点
            while p.rtag == 1: # 如果当前结点有后继，则直接访问后继结点
                p = p.rightChild
                print(p.key, end = " ")
            p = p.rightChild # 如果当前结点没有后继时，进入其右子树

def main():
    mytree = DoubleThreadedBinaryTree() # 创建一个空的二叉树

    # 测试插入构造二叉查找树（默认所有的结点的ltag,rtag=0）
    mytree[5] = "red" # 插入key=3
    mytree[3] = "blue" # 插入key=4
    mytree[7] = "yellow" # 插入key=6
    # mytree[2] = "at" # 插入key=2
    # mytree[4] = "all" # 插入key=2
    # mytree[6] = "try" # 插入key=2
    # mytree[8] = "lan" # 插入key=2
    print(list(mytree.root))  # [2,3,4,5,6,7,8]

    """线索化后不能进行插入和删除，只能遍历（线索化要么中序，要么前序，要么后序，不能叠加）"""
    
    # 测试中序线索化二叉树
    mytree.inThreading()
    print(mytree)
    k5 = mytree.root
    k3 = k5.leftChild
    k7 = k5.rightChild
    # k2 = k3.leftChild
    # k4 = k3.rightChild
    # k6 = k7.leftChild
    # k8 = k7.rightChild
    print(k5.key)
    print(k3.key, k7.key)
    # print(k2.key, k4.key, k6.key, k8.key)



    # 测试中序线索化后的各个结点的引用值是否正确

    print("key = 5 的结点", k5.ltag, k5.leftChild.key, k5.key, k5.rightChild.key, k5.rtag)
    print("key = 3 的结点", k3.ltag, k3.leftChild, k3.key, k3.rightChild, k3.rtag)
    print("key = 7 的结点", k7.ltag, k7.leftChild.key, k7.key, k7.rightChild, k7.rtag)
    # print("key = 2 的结点", k2.ltag, k2.leftChild, k2.key, k2.rightChild, k2.rtag)
    # print("key = 4 的结点", k4.ltag, k4.leftChild.key, k4.key, k4.rightChild, k4.rtag)
    # 测试中序线索化后的中序遍历


if __name__ == '__main__':
    main()