# 数学表达式的解析树
# 数学表达式的树叶是操作数，其他结点为操作符

"""
将一个全括号数学表达式转化为解析树的过程如下：
1、若碰到"("，为当前结点插入左结点，并移动到左结点
2、若碰到“+,-,*,/”，设置当前结点的值为该符号，并为当前结点插入右节点，并移动到右结点
3、若碰到数字，设置当前结点的值为该数字，并移动到其父结点
4、若碰到")"，移动到当前结点的父结点
"""

from binaryTree2 import BinaryTree
import operator

class Stack:

    def __init__(self):
        self.items = []

    # 判断是否为空
    def isEmpty(self):
        return self.items == []

    # 添加item
    def push(self, item):
        self.items.append(item)

    # 删除item
    def pop(self):
        return self.items.pop()

    # 获取top端的item
    def peek(self):
        return self.items[-1]

    # 获取栈中元素个数
    def size(self):
        return len(self.items)

# 构建解析树
def buildParseTree(fpexp):
    # # fpexp: 完全括号表达式且每个符号之间用空格隔开: 例如"( ( ( a + b ) / c ) + d )"
    # fplist = fpexp.split() 

    # 改进，能同时处理带完整的空格，部分空格，和不带空格的情况
    fpexp = fpexp.replace(" ", "") # 去掉字符串中的所有空格
    fplist = [] # 存储符号和正确的数字符号
    i = 0 # i为索引
    numtoken = ["0","1","2","3","4","5","6","7","8","9"]
    while i < len(fpexp):
        if fpexp[i] not in numtoken:
            fplist.append(fpexp[i])
            i = i + 1
        else:
            j = i 
            while fpexp[j] in numtoken:
                j = j + 1
            fplist.append(fpexp[i:j])
            i = j

    pStack = Stack() # 创建一个栈，存放当前结点的父结点
    # 创建一颗空根结点树
    eTree = BinaryTree('')
    # 将此结点压入栈
    pStack.push(eTree)
    # 设置当前结点
    currentTree = eTree

    # 根据中缀表达式构建表达式树
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('') # 插入当前结点的左结点
            pStack.push(currentTree) # 当前结点入栈
            currentTree = currentTree.getLeftChild() # 当前结点指向左结点
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i) # 当前结点的值设置为i
            currentTree.insertRight('') # 插入一个当前结点的右结点
            pStack.push(currentTree) # 将当前结点入栈
            currentTree = currentTree.getRightChild() # 当前结点指向右结点
        elif i == ')':
            currentTree = pStack.pop() # 当前结点指向父结点
        elif i not in ['+', '-', '*', '/', '(', ')']:
            try:
                currentTree.setRootVal(int(i)) # 当前结点的值设置为int(i)
                parent = pStack.pop() # 当前结点的父结点
                currentTree = parent # 当前结点指向父结点
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))
    return eTree

# 前序遍历解析树
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 中序遍历解析树
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# 后序遍历解析树
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# 计算解析树
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC: # 当前结点的左右子结点均非空，则为操作符
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        # 如果左和右结点都为None，那么当前节点是一个叶节点
        return parseTree.getRootVal()

# 使用后序遍历计算解析树
def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

# 计算树高
def height(tree):
    if tree == None:
        return 0
    else:
        return 1 + max(height(tree.leftChild), height(tree.rightChild))                                                                                                      

# 使用中序遍历还原表达式的完全括号版本（这个方法连操作数都有括号）
def printexp(tree):
    sVal = ""
    if tree:
        sVal = "(" + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ")"
    return sVal

# 改进: 使得操作数没有括号
def printexp2(tree):
    if tree.leftChild:
        print('(', end=' ')
        printexp2(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.rightChild:
        printexp2(tree.getRightChild())
        print(')', end=' ')

# 存储中序遍历结果
# def in_order(tree):
#     inlist = []
#     if tree:
#         inlist += in_order(tree.getLeftChild())
#         inlist.append(tree.getRootVal())
#         inlist += in_order(tree.getRightChild())
#     return inlist

def main():
    inString = "( 3 + (4 * 5 ) )"
    print(inString)
    pt = buildParseTree(inString)
    print(evaluate(pt))
    print(postordereval(pt))
    print("\n")
    # preorder(pt)
    # print("\n") 
    # postorder(pt)
    # print("\n")
    # inorder(pt)
    # print("\n")
    # res = in_order(pt)
    # print(res)
    # print("\t")

    print(printexp(pt)) # 输出((3)+((4)*(5)))
    print("\t")

    printexp2(pt) # ( 3 + ( 4 * 5 ) )  
    print("\t")

    # 计算树高
    print(height(pt))

if __name__ == '__main__':
    main()