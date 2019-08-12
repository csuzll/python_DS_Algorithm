# 研究二叉查找树作为从键映射到值的一种方法
# 二叉查找树: 左子树小于父结点，右子树大于父结点，称为bst属性，此属性适用于每个父级和子级
# 左子树中的所有键小于根中的键。 右子树中的所有键都大于根中的键。


class BinarySearchTree:
    def __init__(self):
        self.root = None # 树根
        self.size = 0  # 树的大小

    # 树大小，调用方式为: bst.length()
    def length(self):
        return self.size

    # 重写内置函数__len__()，调用方式为: len(bst)
    def __len__(self):
        return self.size

    # 重写内置函数__iter__()，使得bst可迭代，调用方式为: next(bst)
    def __iter__(self):
        return self.root.__iter__()

    # 将键值对放入树中，并调整保持构成二叉查找树
    def put(self, key, val):
        if self.root: 
            # 树有根，调用私有递归辅助函数_put()
            self._put(key, val, self.root)
        else:
            # 没有根，创建一个新的TreeNode作为树的根
            self.root = TreeNode(key, val)

    def _put(self, key, val, currentNode):
        if key == currentNode.key: # 新键等于当前结点的键，修改当前结点的payload
            currentNode.payload = val
        elif key < currentNode.key: # 新键小于当前结点的键，搜索左子树
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                # 当前结点的左结点设置为新建
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else: # 新键大于当前结点的键，搜索右子树
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                # 当前结点的右结点设置为新键
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    # 重写内置函数__setitem__()，调用方式: bst[key] = val
    def __setitem__(self, k, v):
        self.put(k, v)

    # 获取键对应的值
    def get(self, key):
        if self.root: # 存在树
            res = self._get(self, key, self.root)
            if res: # 找到了
                return res.payload
            else: # 不存在
                return None
        else: # 空树
            return None

    def _get(self, key, currentNode):
        # 返回一个treeNode或者None
        if not currentNode: # 不存在
            return None
        else currentNode.key == key: # 相等
            return currentNode
        elif key < currentNode.key: # 小于，递归查找左子树
            return self._get(key, currentNode.leftChild)
        else: # 大于，递归查找右子树
            return self._get(key, currentNode.rightChild)

    # 重写内置函数__getitem__()，调用方式: val = bst[key]
    def __getitem__(self, key):
        return self.get(key)

    # 重写内置函数__contains__()，调用方式: if key in bst ....
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    # 删除指定的键值对
    def delete(self, key):
        if self.size > 1: # 树有多个结点
            nodeToRemove = self._get(key, self.root) # 查找要删除的结点
            if nodeToRemove: # 找到
                self.remove(nodeToRemove)
                self.size -= 1
            else: # 没找到
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key: # 树只有一个结点，且与要删除的键相等
            self.root = None
            self.size = self.size - 1
        else: # 树只有一个结点，且与要删除的键不等
            raise KeyError("Error, key not in tree")

    # 移除函数(size>1的树中的结点的移除)
    def remove(self, currentNode):
        if currentNode.isLeaf(): # 当前结点为叶子结点，没有子结点
            # 删除当前结点并删除当前结点的父结点对该结点的引用
            if currentNode == currentNode.parent.leftChild: # 当前结点为左叶子结点
                currentNode.parent.leftChild = None 
            else: # 当前结点为为右叶子结点
                currentNode.parent.rightChild = None
        else currentNode.hasBothChildren(): # 当前结点有两个子结点
            succ = currentNode.findSuccessor() # 找到当前结点的后继结点
            succ.spliceOut() # 删除后继结点
            currentNode.key = succ.key # 当前结点的key设置为后继结点的key
            currentNode.payload = succ.payload # 当前结点的payload设置为后继结点的payload
        else: # 当前结点有1个子结点
            if currentNode.hasLeftChild(): # 当前结点的子结点为左子结点
                if currentNode.isLeftChild(): # 当前结点为其父结点的左子结点
                    currentNode.leftChild.parent = currentNode.parent # 当前结点的左子结点的父引用指向当前结点的父结点
                    currentNode.parent.leftChild = currentNode.leftChild # 当前结点的父结点的左子结点引用指向当前结点的左子结点
                elif currentNode.isRightChild(): # 当前结点为其父结点的右子结点
                    currentNode.leftChild.parent = currentNode.parent # 当前结点的左子结点的父引用指向当前结点的父结点
                    currentNode.parent.rightChild = currentNode.leftChild # 当前结点的父结点的右子结点引用指向当前结点的左子结点
                else: # 当前结点没有父级，即它是根
                    # 在根上调用replaceNodeData方法来替换key,payload,leftchild,rightchild
                    currentNode.replaceNodeData(currentNode.leftChild.key, 
                        currentNode.leftChild.payload, 
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild)
            else: # 当前结点的子结点为右子结点
                if currentNode.isLeftChild(): # 当前结点为其父结点的右子结点
                    currentNode.rightChild.parent = currentNode.parent # 当前结点的右子结点的父引用指向当前结点的父结点
                    currentNode.parent.leftChild = currentNode.rightChild # 当前结点的父结点的左子结点引用指向当前结点的右子结点
                elif currentNode.isRightChild(): # 当前结点为其父结点的右子结点
                    currentNode.rightChild.parent = currentNode.parent # 当前结点的右子结点的父引用指向当前结点的父结点
                    currentNode.parent.rightChild = currentNode.rightChild # 当前结点的父结点的右子结点引用指向当前结点的右子结点
                else: # 当前结点没有父级，即它是根
                    # 在根上调用replaceNodeData方法来替换key,payload,leftchild,rightchild
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)


    # 子树中的最小键(任何二叉查找树中的最小值键是树的最左子结点。)
    def findMin(self):
        current = self
        # 通过简单地循环树中每个节点的左子结点，直到它到达没有左子结点的结点
        while current.hasLeftChild:
            current = current.leftChild
        return current

    # 找当前结点的后继结点
    def findSuccessor(self):
        succ = None
        if self.hasRightChild(): # 结点有右子结点
            # 后继结点为右子树中的最小值
            succ = self.rightChild.findMin()
        else: # 没有右子结点
            if self.parent: 
                if self.isLeftChild(): # 是父结点的左子结点
                    # 后继结点为父结点
                    succ = self.parent
                else: # 是父结点的右子结点
                    # 后继结点为此结点的父结点的后继结点(不包括此结点)
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    # 删除后继结点
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.rightChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    # 重写内置函数__delitem__()，调用方式: del bst[key]
    def __delitem__(self, key):
        self.delete(key)

# 结点类
class TreeNode:
    """ A node for the Binary Search Tree """
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key # 键
        self.payload = val # 值
        self.leftChild = left # 左孩子
        self.rightChild = right # 右孩子
        self.parent = parent # 双亲

    # 返回左孩子，可用于判断一个结点是否有左孩子
    def hasLeftChild(self):
        return self.leftChild

    # 返回右孩子，可用于判断一个结点是否有右孩子
    def hasRightChild(self):
        return self.rightChild

    # 判断结点是否是左孩子
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    # 判断结点是否是右孩子
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # 判断是否是树根
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


def main():
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])