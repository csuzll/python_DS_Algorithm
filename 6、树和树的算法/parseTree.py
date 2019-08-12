from binaryTree import BinaryTree
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
    # fpexp: 完全括号表达式
    fplist = fpexp.split() 
    pStack = Stack() # 创建一个栈，存放当前结点的父结点
    # 创建一颗空根结点树
    eTree = BinaryTree('')
    # 将此结点压入栈
    pStack.push(eTree)
    # 设置当前结点
    currentTree = eTree

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

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i)) # 当前结点的值设置为int(i)
                parent = pStack.pop() # 当前结点的父结点
                currentTree = parent # 当前结点指向父结点

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

# 计算解析树
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        # 如果左和右结点都为None，那么当前节点是一个叶节点
        return parseTree.getRootVal()

# 前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 中序遍历
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# 后序遍历
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

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

# 使用中序遍历还原表达式的完全括号版本
def printexp(tree):
    sVal = ""
    if tree:
        sVal = "(" + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ")"
    return sVal

inString = "( ( 10 + 5 ) * 3 )"
print(inString)
pt = buildParseTree(inString)
print(evaluate(pt))
print(postordereval(pt))
print("\n")
preorder(pt)
print("\n") 
postorder(pt)
print("\n")
inorder(pt)
print("\n")
print(printexp(pt))


