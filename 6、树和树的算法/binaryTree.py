'''
	This is an example of a BinaryTree data structure 
	built as a class 
	
	This example will only work if the rootObj passed into the
	class is a python primitive data type.

	使用class构建二叉树
'''
class BinaryTree:
	# 初始化，创建以rootObj为根植的树
	# 此时，左右子树均为空
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	# 插入左子结点
	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			# 插入的左子节点的左子结点设置为原树的左子结点
			t.leftChild = self.leftChild 
			# 原树的左子结点设置为新的左子结点
			self.leftChild = t

	# 插入右子结点
	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	# 前序遍历,（中，左，右）
	def preorder(self):
		print(self.key)
		if self.leftChild:
			self.leftChild.preorder()
		if self.rightChild:
			self.rightChild.preorder()

	# 后序遍历，（左，右，中）
	def postorder(self):
		if self.leftChild:
			self.leftChild.postorder()
		if self.rightChild:
			self.rightChild.postorder()
		print(self.key)

	# 中序遍历，（左，中，右）
	def inorder(self):
		if self.leftChild:
			self.leftChild.inorder()
		print(self.key)
		if self.rightChild:
			self.rightChild.inorder()
			
	# 获取左结点
	def getLeftChild(self):
		return self.leftChild

	# 获取右结点
	def getRightChild(self):
		return self.rightChild

	# 获取根结点值
	def getRootVal(self):
		return self.key

	# 设置根结点值
	def setRootVal(self, obj):
		self.key = obj

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

if __name__ == '__main__':
	main()