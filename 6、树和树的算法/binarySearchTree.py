# 研究二叉查找树作为从键映射到值的一种方法
# 二叉查找树: 树上任一结点，该结点的值都大于它的非空左子树的值，都小于它的非空右子树的值。
# 任一结点的左右子树都是二叉查找树
# 中序遍历二叉查找树能够按从小到大的顺序遍历二叉树

from treeNode import TreeNode

# 二叉查找树类
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

    # 重写内置函数__iter__()，使得bst可迭代
    def __iter__(self):
        # 在结点类中实现迭代
        return self.root.__iter__()

    # 将键值对放入树中，并调整保持二叉查找树属性
    """ put的性能: 取决于树的高度"""
    def put(self, key, val):
        if self.root: 
            # 树有根，调用私有递归辅助函数_put()
            self._put(key, val, self.root)
        else:
            # 没有根，创建一个新的TreeNode作为树的根
            self.root = TreeNode(key, val)
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
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.size += 1
        else: # 新键大于当前结点的键，搜索右子树
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                # 当前结点的右结点设置为新键
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.size += 1

    # 重写内置函数__setitem__()，调用方式: bst[key] = val
    def __setitem__(self, k, v):
        self.put(k, v)

    # 获取键对应的值
    def get(self, key):
        if self.root: # 存在树
            res = self._get(key, self.root)
            if res: # 找到key
                return res.payload
            else: # 没找到key
                return None
        else: # 空树
            return None

    # 树存在时的查找函数
    def _get(self, key, currentNode):
        # 返回一个treeNode或者None
        if not currentNode: # 不存在
            return None
        elif currentNode.key == key: # 相等
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
            nodeToRemove = self._get(key, self.root) # 找到要删除的结点
            if nodeToRemove: # 找到
                self.remove(nodeToRemove) # 调用remove函数
                self.size -= 1
            else: # 没找到
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key: # 树只有一个结点，且与要删除的键相等
            self.root = None # 树变为空树
            self.size = self.size - 1
        else: # 树只有一个结点，且与要删除的键不等
            raise KeyError("Error, key not in tree")

    # 移除函数(size>1的树中的结点的移除)
    def remove(self, currentNode):
        if currentNode.isLeaf(): # 当前结点为叶子结点
            # 删除当前结点并置空当前结点的父结点对该结点的引用
            if currentNode == currentNode.parent.leftChild: # 当前结点为左叶子结点
                currentNode.parent.leftChild = None 
            else: # 当前结点为为右叶子结点
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): # 当前结点有两个子结点
            # 使用当前结点的左子树中的最右子结点(左子树中的最大值:前驱结点)，或者当前结点的右子树中的最左子结点(右子树中的最小值: 后继结点))替换被删除的结点
            # 这里使用的是要删除的结点的右子树中的最小值来替换
            succ = currentNode.findSuccessor() # 找到当前结点的后继结点
            succ.spliceOut() # 删除后继结点(后继结点要么只有1个子结点要么没有)
            currentNode.key = succ.key # 当前结点的key设置为后继结点的key
            currentNode.payload = succ.payload # 当前结点的payload设置为后继结点的payload
        else: # 当前结点只有1个子结点
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

    # 重写内置函数__delitem__()，调用方式: del bst[key]
    def __delitem__(self, key):
        self.delete(key)

    # 利用TreeNode的findSuccessor()后继结点来写一个非递归的二叉搜索树的中序遍历
    def inorderSucc(self):
        if self.size > 0: # 非空树
            # inlist = [] # 中序遍历结果
            node = self.root
            while node.leftChild != None:
                node = node.leftChild
            while node:
                # inlist.append(node.key)
                print(node.key, end=" ")
                node = node.findSuccessor()
            # return inlist
        else: # 空树
            print("None")
            # return None     

    # 利用TreeNode的findPredecessor前驱结点来写一个非递归的二叉搜索树的中序遍历的倒序
    def inorderPrec(self):
        if self.size > 0: # 非空树
            # inlist = [] # 中序遍历结果
            node = self.root
            while node.rightChild != None:
                node = node.rightChild
            while node:
                # inlist.insert(0, node.key)
                print(node.key, end=" ")
                node = node.findPredecessor()
            # return inlist
        else: # 空树
            print("None")
            # return None

    # 二叉搜索树的前序遍历
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tree):
        if tree:
            print(tree.key, end=" ")            
            self._preorder(tree.leftChild)
            self._preorder(tree.rightChild)

    # 二叉搜索树的中序遍历
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tree):
        if tree:
            self._inorder(tree.leftChild)
            print(tree.key, end=" ")
            self._inorder(tree.rightChild)

    # 二叉搜索树的后序遍历
    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tree):
        if tree:
            self._postorder(tree.rightChild)
            self._postorder(tree.leftChild)
            print(tree.key, end=" ")

    # 二叉搜索树的层次遍历
    def traverse(self):
        row = [self.root]
        while row:
            print([i.key for i in row]) # 输出当前层的结点
            temp = [] # 存储了下一层的所有结点
            for node in row:
                if node.leftChild:
                    temp.append(node.leftChild)
                if node.rightChild:
                    temp.append(node.rightChild)
            row = temp

def main():
    mytree = BinarySearchTree() # 创建一个空的二叉树

    # 测试插入
    mytree[3] = "red" # 插入key=3
    mytree[4] = "blue" # 插入key=4
    mytree[6] = "yellow" # 插入key=6
    mytree[2] = "at" # 插入key=2

    # 测试获取
    print("key 6: ", mytree[6]) # 获取key=6对应的值
    print("key 2: ", mytree[2]) # 获取key=2对应的值

    # 测试length()
    print("my tree's length: ", mytree.length())

    # 测试插入相同的key
    mytree[2] = "green"

    # 测试len()
    print("my tree's length: ", len(mytree))
    print("key 2: ", mytree[2])

    # 测试in操作__contain__()
    if 6 in mytree:
        print("Yes")

    # for ... in ...其实隐式调用了类中的__iter__()方法
    # 只有实现了__iter__()方法才能使用for ... in ...语句
    for key in mytree: # 输出 2 3 4 6
        print(key)

    # mytree实现了__iter__()方法，则mytree为可迭代对象
    print(list(mytree)) # 输出[2,3,4,6]
    print(list(mytree.root)) # 输出[2,3,4,6]
    print("\n")

    # 测试删除
    # del mytree[6] # 删除的6为叶子结点
    # print(list(mytree)) # 输出[2,3,4]
    # del mytree[4] # 删除的4有一个子结点
    # print(list(mytree)) # 输出[2,3,6]
    # del mytree[3] # 删除的3有两个子结点
    # print(list(mytree)) # 输出[2,4,6]

    # 中序后继结点实现中序遍历测试
    mytree.inorderSucc()
    print("\n")

    # 中序前驱结点实现中序遍历倒序测试
    mytree.inorderPrec()
    print("\n")

    # 中序，前序，后序
    mytree.inorder()
    print("\t")
    mytree.preorder()
    print("\t")
    mytree.postorder()
    print("\t")

    # 测试遍历
    mytree.traverse()

if __name__ == '__main__':
    main()