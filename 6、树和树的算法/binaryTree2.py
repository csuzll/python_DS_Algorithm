# 直接构建二叉树类，此类包含结点值，左孩子，右孩子属性。

'''
    This is an example of a BinaryTree data structure 
    built as a class 
    
    This example will only work if the rootObj passed into the
    class is a python primitive data type.

    使用class构建二叉树
'''

class BinaryTree:
    def __init__(self, rootObj, leftChild=None, rightChild=None):
        self.key = rootObj
        self.leftChild = leftChild
        self.rightChild = rightChild

    # 插入左结点
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # 插入右结点
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # 判断是否为叶子结点
    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key =obj

    def getRootVal(self):
        return self.key

    # 递归前序
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    # 递归中序
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    # 递归后序
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)


def main():
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())


    # 按例子生成一棵树
    # a(b(None, d), c(e, f))
    def buildTree():
        b = BinaryTree("a")
        b.insertLeft("b")
        b.insertRight("c")

        b.getLeftChild().insertRight("d")

        b.getRightChild().insertLeft("e")
        b.getRightChild().insertRight("f")

        return b

    ttree = buildTree()
    print(ttree.getRootVal())
    print(ttree.getLeftChild().getRootVal())
    print(ttree.getRightChild().getRootVal())

    print(ttree.getLeftChild().getRightChild().getRootVal())

    print(ttree.getRightChild().getLeftChild().getRootVal())
    print(ttree.getRightChild().getRightChild().getRootVal())

    print("\n")

    # 测试中序遍历
    ttree.inorder()

    # 根据前序遍历序列和中序遍历序列构建树
    pre = [4,3,5,10,8,9,7,12]
    mid = [3,5,10,8,4,9,7,12]
    def build(pre, mid):
        if not pre:
            return None
        tree = BinaryTree(pre[0]) # 根
        index = mid.index(pre[0]) # 根在中序序列中的位置
        tree.leftChild = build(pre[1:index+1], mid[:index]) # 左子树
        tree.rightChild = build(pre[index+1:], mid[index+1:]) # 右子树
        return tree
    tt = build(pre, mid)
    tt.preorder()

    # 判断两颗树是否相同
    t1 = BinaryTree(4,BinaryTree(3,BinaryTree(5,BinaryTree(10)),BinaryTree(8)),BinaryTree(9,BinaryTree(7),BinaryTree(12)))    
    t2 = BinaryTree(4,BinaryTree(3,BinaryTree(5,BinaryTree(10)),BinaryTree(8)),BinaryTree(9,BinaryTree(7),BinaryTree(12)))    
    t3 = BinaryTree(4,BinaryTree(3,BinaryTree(8,BinaryTree(40)),BinaryTree(13)),BinaryTree(9,BinaryTree(7),BinaryTree(12)))
    def is_same_tree(tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        elif tree1 and tree2:
            return tree1.key == tree2.key and is_same_tree(tree1.leftChild, tree2.leftChild) and is_same_tree(tree1.rightChild, tree2.rightChild)
        else:
            return False
    print(is_same_tree(t1, t2))
    print(is_same_tree(t1, t3))


if __name__ == '__main__':
    main()