# 继承于二叉搜索树
# 并修改TreeNode增加balanceFactor属性

from binarySearchTree import BinarySearchTree
from treeNode import TreeNode

class AvlTree(BinarySearchTree):
    # 重写私有方法_put()
    def _put(self, key, val, currentNode):
        if key == currentNode.key: # 键相等
            currentNode.replaceNode(key, val, currentNode.leftChild, currentNode.rightChild)
        elif key < currentNode.key: # 键小于当前结点的键
            if currentNode.hasLeftChild(): # 当前结点有左孩子
                self._put(key, val, currentNode.leftChild)
            else: # 无左孩子
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild) # 调用更新平衡因子且保持平衡
                self.size += 1
        else: # 键大于当前结点的键
            if currentNode.hasRightChild(): # 当前结点有右孩子
                self._put(key, val, currentNode.rightChild)
            else: # 无右孩子
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild) # 调用更新平衡因子且保持平衡
                self.size += 1

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
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

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

if __name__ == '__main__':
    main()