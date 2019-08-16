# 继承于二叉搜索树
# 并修改TreeNode增加balanceFactor属性

from binarySearchTree import BinarySearchTree
from treeNode import TreeNode

class AvlNode(TreeNode):
    def __init__(self, key, val, left=None, right=None, parent=None):
        TreeNode.__init__(self, key, val, left, right, parent)

        self.balanceFactor = 0 # 平衡因子（左子树-右子树）

class AvlTree(BinarySearchTree):

    # 重写二叉树的插入，使得插入时能形成平衡二叉树
    # 将键值对放入树中，并调整保持平衡二叉查找树属性
    def put(self, key, val):
        if self.root: 
            # 树有根，调用私有递归辅助函数_put()
            self._put(key, val, self.root)
        else:
            # 没有根，创建一个新的TreeNode作为树的根
            self.root = AvlNode(key, val)
            self.size += 1
    
    def _put(self, key, val, currentNode):
        if key == currentNode.key: # 键相等
            currentNode.replaceNode(key, val, currentNode.leftChild, currentNode.rightChild)
        elif key < currentNode.key: # 键小于当前结点的键
            if currentNode.hasLeftChild(): # 当前结点有左孩子
                self._put(key, val, currentNode.leftChild)
            else: # 无左孩子
                currentNode.leftChild = AvlNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild) # 调用更新平衡因子且保持平衡
                self.size += 1
        else: # 键大于当前结点的键
            if currentNode.hasRightChild(): # 当前结点有右孩子
                self._put(key, val, currentNode.rightChild)
            else: # 无右孩子
                currentNode.rightChild = AvlNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild) # 调用更新平衡因子且保持平衡
                self.size += 1

    # # 重写remove方法，使得删除结点时能形成平衡二叉树（还有点问题）
    # def remove(self, currentNode):
    #     if currentNode.isLeaf(): # 当前结点为叶子结点
    #         # 删除当前结点并置空当前结点的父结点对该结点的引用
    #         if currentNode == currentNode.parent.leftChild: # 当前结点为左叶子结点
    #             currentNode.parent.leftChild = None
    #             currentNode.parent.balanceFactor -= 1 # 当前结点的父结点的平衡因子减1 
    #         else: # 当前结点为为右叶子结点
    #             currentNode.parent.rightChild = None
    #             currentNode.parent.balanceFactor += 1 # 当前结点的父结点的平衡因子加1 
    #         # 判断父结点的平衡因子
    #         if currentNode.parent.balanceFactor > 1 or currentNode.parent.balanceFactor < -1:
    #             self.rebalance(currentNode.parent)
    #     elif currentNode.hasBothChildren(): # 当前结点有两个子结点
    #         # 使用当前结点的左子树中的最右子结点(左子树中的最大值:前驱结点)，或者当前结点的右子树中的最左子结点(右子树中的最小值: 后继结点))替换被删除的结点
    #         # 这里使用的是要删除的结点的右子树中的最小值来替换
    #         succ = currentNode.findSuccessor() # 找到当前结点的后继结点
    #         # 先更新后继结点的父结点的平衡因子
    #         if succ.isLeftChild():
    #             succ.parent.balanceFactor -= 1
    #         elif succ.isRightChild():
    #             succ.parent.balanceFactor += 1
    #         succ.spliceOut() # 删除后继结点(后继结点要么只有1个子结点要么没有)
    #         currentNode.key = succ.key # 当前结点的key设置为后继结点的key
    #         currentNode.payload = succ.payload # 当前结点的payload设置为后继结点的payload
    #         # 删除后，再判断是否需要平衡，然后进行再平衡操作
    #         if succ.parent.balanceFactor > 1 or succ.parent.balanceFactor < -1:
    #             self.rebalance(succ.parent)
    #     else: # 当前结点只有1个子结点
    #         # 先更新parent的balancefactor
    #         if currentNode.isLeftChild():
    #             currentNode.parent.balanceFactor -= 1
    #         elif currentNode.isRightChild():
    #             currentNode.parent.balanceFactor += 1

    #         if currentNode.hasLeftChild(): # 当前结点的子结点为左子结点
    #             if currentNode.isLeftChild(): # 当前结点为其父结点的左子结点
    #                 currentNode.leftChild.parent = currentNode.parent # 当前结点的左子结点的父引用指向当前结点的父结点
    #                 currentNode.parent.leftChild = currentNode.leftChild # 当前结点的父结点的左子结点引用指向当前结点的左子结点
    #             elif currentNode.isRightChild(): # 当前结点为其父结点的右子结点
    #                 currentNode.leftChild.parent = currentNode.parent # 当前结点的左子结点的父引用指向当前结点的父结点
    #                 currentNode.parent.rightChild = currentNode.leftChild # 当前结点的父结点的右子结点引用指向当前结点的左子结点
    #             else: # 当前结点没有父级，即它是根
    #                 # 在根上调用replaceNodeData方法来替换key,payload,leftchild,rightchild
    #                 currentNode.replaceNodeData(currentNode.leftChild.key, 
    #                     currentNode.leftChild.payload, 
    #                     currentNode.leftChild.leftChild,
    #                     currentNode.leftChild.rightChild)
    #         else: # 当前结点的子结点为右子结点
    #             if currentNode.isLeftChild(): # 当前结点为其父结点的右子结点
    #                 currentNode.rightChild.parent = currentNode.parent # 当前结点的右子结点的父引用指向当前结点的父结点
    #                 currentNode.parent.leftChild = currentNode.rightChild # 当前结点的父结点的左子结点引用指向当前结点的右子结点
    #             elif currentNode.isRightChild(): # 当前结点为其父结点的右子结点
    #                 currentNode.rightChild.parent = currentNode.parent # 当前结点的右子结点的父引用指向当前结点的父结点
    #                 currentNode.parent.rightChild = currentNode.rightChild # 当前结点的父结点的右子结点引用指向当前结点的右子结点
    #             else: # 当前结点没有父级，即它是根
    #                 # 在根上调用replaceNodeData方法来替换key,payload,leftchild,rightchild
    #                 currentNode.replaceNodeData(currentNode.rightChild.key,
    #                     currentNode.rightChild.payload,
    #                     currentNode.rightChild.leftChild,
    #                     currentNode.rightChild.rightChild)
    #         # 删除后，再判断是否再平衡，然后进行再平衡操作
    #         if currentNode.parent != None:
    #             if currentNode.parent.balanceFactor > 1 or currentNode.parent.balanceFactor < -1:
    #                 self.rebalance(currentNode.parent)

    # 更新平衡因子
    def updateBalance(self, node):
        """对插入元素的父结点递归地更新平衡因子，直到：1.已经更新到root；2.当前父结点的平衡因子是0。"""
        if node.balanceFactor > 1 or node.balanceFactor < -1: # 如果平衡因子大于1或小于-1，需要重新平衡
            self.rebalance(node) # 重新平衡
            return
        # 不需要重新平衡，只需更新受影响的结点的平衡因子
        if node.parent != None: # node的父结点不为空
            if node.isLeftChild(): # 插入的node为左子结点
                node.parent.balanceFactor += 1  # 父结点平衡因子加1
            elif node.isRightChild(): # 插入的node为右子结点
                node.parent.balanceFactor -= 1  # 父结点平衡因子减1

            if node.parent.balanceFactor != 0: # 如果父结点的平衡因子不为0，则继续递归调用更新平衡因子
                self.updateBalance(node.parent)

    # 重新平衡
    def rebalance(self, node):
        if node.balanceFactor < 0: # 右重需左旋
            if node.rightChild.balanceFactor > 0: # 结点的右子结点左重，右子结点需先右旋
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0: # 左重需右旋
            if node.leftChild.balanceFactor < 0: # 结点的左子结点右重，左子结点需先左旋
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    # 左旋操作
    def rotateLeft(self, rotRoot):
        """rotRoot为要重新平衡的子树的根"""
        """修改不涉及旧根的左孩子和新根的右孩子"""

        # 1、修改子树的新根为旧根的右孩子（使用临时变量newRoot）
        newRoot = rotRoot.rightChild

        # 2、修改旧根的右孩子指向新根的左孩子
        rotRoot.rightChild = newRoot.leftChild

        # 3、如果新根原来存在左孩子，则修改这个孩子的父亲指向旧根
        if newRoot.leftChild != None: 
            newRoot.leftChild.parent = rotRoot # 新根的左孩子的新父亲变为旧根

        # 4、修改旧根的父亲指向新根（新根可能是旧根父亲的左孩子或右孩子）
        newRoot.parent = rotRoot.parent # 新根的父结点设置为旧根的父结点
        if rotRoot.isRoot(): # 旧根是整个树的根
            self.root = newRoot # 修改整个树的根引用指向新根
        else:
            if rotRoot.isLeftChild(): 
                rotRoot.parent.leftChild = newRoot # 旧根的父亲的左孩子变为新根
            else:
                rotRoot.parent.rightChild = newRoot # 旧根的父亲的右孩子变为新根

        # 5、修改新根的左孩子为旧根，旧根的父结点为新根
        newRoot.leftChild = rotRoot 
        rotRoot.parent = newRoot 

        # 6、修改新根和旧根的平衡因子
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    # 右旋操作
    def rotateRight(self, rotRoot):
        """rotRoot为要重新平衡的子树的根"""
        """修改不涉及旧根的右孩子和新根的左孩子"""

        # 1、修改子树的新根为旧根的左孩子
        newRoot = rotRoot.leftChild

        # 2、修改旧根的左孩子指向新根的右孩子
        rotRoot.leftChild = newRoot.rightChild

        # 3、如果新根原来存在右孩子，则修改整个孩子的父亲指向旧根
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot

        # 4、修改旧根的父亲指向新根（新根可能是旧根父亲的左孩子或右孩子）
        newRoot.parent = rotRoot.parent
        if rotRoot.parent.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot

        # 5、修改新根的右孩子为旧根，旧根的父结点为新根
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot

        # 6、修改新根和旧根的平衡因子
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

def main():
    mytree = AvlTree() # 创建一个空的二叉树

    # 测试插入
    mytree[3] = "red" # 插入key=3
    mytree[4] = "blue" # 插入key=4
    mytree[6] = "yellow" # 插入key=6
    mytree[2] = "at" # 插入key=2

    # 测试key的遍历输出
    print(list(mytree)) # 输出[2,3,4,6]

    # 测试根结点平衡因子
    print(mytree.root.key, mytree.root.balanceFactor) # 4, 1
    # 测试3和6的平衡因子
    if mytree.root.hasLeftChild():
        print(mytree.root.leftChild.key, mytree.root.leftChild.balanceFactor) # 3, 1
    if mytree.root.hasRightChild():
        print(mytree.root.rightChild.key, mytree.root.rightChild.balanceFactor) # 6, 0
    # 测试2的平衡因子
    print(mytree.root.leftChild.leftChild.key, mytree.root.leftChild.leftChild.balanceFactor) # 2, 0
    # 通过平衡因子的测试，构建avl树没有问题。

    # # 删除一个结点并查看树的平衡因子（还有点问题）
    # del mytree[2]
    # print(list(mytree))
    # print(mytree.root.key, mytree.root.balanceFactor)
    # print(mytree.root.leftChild.key, mytree.root.leftChild.balanceFactor)
    # print(mytree.root.rightChild.key, mytree.root.rightChild.balanceFactor)

if __name__ == '__main__':
    main()