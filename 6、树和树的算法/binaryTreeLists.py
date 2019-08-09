'''
	This is an example of a binary tree data structure created with 
	python lists as the underlying data structure.

	不会构造二叉树类，写的函数只是帮助操纵一个标准列表，就像正在使用一棵树。
'''
# 简单地构造一个具有根节点和两个子列表为空的列表。
def BinaryTree(r):
	return [r, [], []]

# 插入左子结点
def insertLeft(root, newBranch):
	t = root.pop(1) # 当前root的左子结点列表
	if len(t) > 1: 
		# t作为新的左子结点的左子结点
		root.insert(1, [newBranch, t, []])
	else: # 当前root的左子结点列表为空
		root.insert(1, [newBranch, [], []])
	return root

# 插入右子结点
def insertRight(root, newBranch):
	t = root.pop(2) # 当前root的右子结点列表
	if len(t) > 1:
		# t作为新的右子结点的右子结点
		root.insert(2, [newBranch, [], t])
	else: # 当前root的右子结点列表为空
		root.insert(2, [newBranch, [], []])
	return root

# 获取根结点的值
def getRootVal(root):
	return root[0]

# 设置根结点的值
def setRootVal(root, newVal):
	root[0] = newVal

# 获取左子树
def getLeftChild(root):
	return root[1]

# 获取右子树
def getRightChild(root):
	return root[2]


r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))


# 按例子生成一棵树
# a(b(None, d), c(e, f))
def buildTree():
	b = BinaryTree("a")
	# Build up the left side of this tree
	insertLeft(b,'b')
	insertRight(getLeftChild(b),'d')

	# Build up the right side of this tree
	insertRight(b,'c')
	insertLeft(getRightChild(b),'e')
	insertRight(getRightChild(b),'f')

	return b

ttree = buildTree()
print(ttree)