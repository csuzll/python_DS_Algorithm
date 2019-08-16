class Node:
	"""结点类"""
	def __init__(self, elem, lchild=None, rchild=None):
		self.elem = elem # 结点值
		self.lchild = lchild # 左孩子结点
		self.rchild = rchild # 右孩子结点

class BinaryTree:
	"""二叉树类"""
	def __init__(self, root=None):
		self.root = root

	# 插入结点
	def insert(self, elem):
		"""
		1、判断根结点是否存在，如果不存在则插入根结点，否则；
		2、从根结点开始，判断左子结点是否存在，如果不存在插入, 否则判断右结点，不存在插入。
		3、如果左右结点存在，再依次遍历左右子结点的子结点，直到插入成功。

		PS: 这样的插入方法构造的二叉树永远是完全二叉树。
		"""
		node = Node(elem)
		if not self.root: # 不存在
			self.root = node
		else:
			node_queue = [self.root] # 保存结点的队列
			while node_queue: # 结点队列非空
				curNode = node_queue.pop(0)
				if not curNode.lchild: # 左子结点不存在
					curNode.lchild = node
					break
				elif not curNode.rchild: # 右子结点不存在
					curNode.rchild = node
					break
				else: # 左右子结点都存在
					node_queue.append(curNode.lchild)
					node_queue.append(curNode.rchild)

	# 宽度优先: 层次遍历
	def bread_travel(self):
		"""利用队列，依次将根，左子树，右子树存入队列，按照队列的先进先出规则来实现层次遍历"""
		if not self.root: # 不存在
			return
		else:
			queue = [self.root] # queue队列，保存结点
			while queue:
				# 弹出队首结点
				curNode = queue.pop(0) 
				print(curNode.elem, end=" ")
				# 如果该结点存在左子结点，则加入队列
				if curNode.lchild: 
					queue.append(curNode.lchild)
				# 如果该结点存在右子结点，则加入队列
				if curNode.rchild: 
					queue.append(curNode.rchild)

	# 深度优先: 递归前序遍历
	def preorder(self, node):
		"""先访问根节点，再先序遍历左子树，然后再先序遍历右子树。总的来说是根—左—右"""
		if node is None:
			return
		else:
			print(node.elem, end=" ")
			self.preorder(node.lchild)
			self.preorder(node.rchild)

	# 深度优先: 递归中序遍历
	def inorder(self, node):
		"""先中序访问左子树，然后访问根，最后中序访问右子树。总的来说是左—根—右"""
		if node is None:
			return
		else:
			self.inorder(node.lchild)
			print(node.elem, end=" ")
			self.inorder(node.rchild)

	# 深度优先: 递归后序遍历
	def postorder(self, node):
		"""先后序访问左子树，然后后序访问右子树，最后访问根。总的来说是左—右—根"""
		if node is None:
			return
		else:
			self.postorder(node.lchild)
			self.postorder(node.rchild)
			print(node.elem, end=" ")

	# 深度优先: 非递归前序遍历(栈实现)
	def pre_order(self):
		"""利用栈，先将根入栈，再将根出栈，并将根的右子树，左子树存入栈，按照栈的后进先出规则来实现非递归前序遍历"""
		if self.root is None:
			return None
		else:
			# node_stack保存未访问的结点
			node_stack = [self.root]
			while len(node_stack) > 0:
				curNode = node_stack.pop()
				print(curNode.elem, end=" ")
				if curNode.rchild: # 右子树
					node_stack.append(curNode.rchild)
				if curNode.lchild: # 左子树
					node_stack.append(curNode.lchild)

	# 深度优先: 非递归中序遍历(栈实现)
	def in_order(self):
		"""利用栈，先将根入栈，左子树入栈，再将左子树出栈，根出栈，最后右子树存入栈，按照栈的后进先出规则来实现非递归中序遍历"""
		if self.root is None:
			return None
		else:
			node_stack = []
			node = self.root
			while node is not None or len(node_stack) > 0:
				if node is not None:
					node_stack.append(node)
					node = node.lchild
				else:
					node = node_stack.pop()
					print(node.elem, end=" ")
					node = node.rchild

	# 深度优先: 非递归后序遍历(两个栈实现)
	def post_order(self):
		"""利用两个栈，第一个栈进栈顺序为左，右，根，第二个栈存储为第一个栈的每个弹出依次进栈，最后第二个栈依次出栈"""
		if self.root is None:
			return None
		else:
			stack1 = [self.root] # 进栈顺序: 左，右，根
			stack2 = [] # 进栈顺序: 根，右，左
			while len(stack1) > 0:
				node = stack1.pop()
				stack2.append(node)
				if node.lchild:
					stack1.append(node.lchild)
				if node.rchild:
					stack1.append(node.rchild)
			# stack2依次出栈
			while len(stack2) > 0:
				print(stack2.pop().elem, end=" ")

	# 递归统计二叉树结点个数
	def nodeCount(self, node):
		"""二叉树结点个数 = 1 + 根的左子树结点个数 + 根的右子树结点个数"""
		if node is None:
			return 0
		else:
			return 1 + self.nodeCount(node.lchild) + self.nodeCount(node.rchild)

	# 递归计算二叉树的高度
	def treeDepth(self, node):
		"""二叉树的高度 h = max(根的左子树高度，根的右子树高度) + 1"""
		if node is None:
			return 0
		else:
			ldepth = self.treeDepth(node.lchild)
			rdepth = self.treeDepth(node.rchild)
			return max(ldepth, rdepth) + 1

	# 非递归求二叉树的高度
	def tree_Depth(self):
		"""利用层次遍历实现
		1. 如果树为空，返回0
		2. 从根结点开始，将根结点加入队列
		3. 当队列非空，记录当前队列的元素个数(上一层结点数)。将上层结点依次出队，如果左右结点
		   都存在，依次入队。直至上层结点出队完成，高度加1。继续第三步，直到队列完全为空。
		"""
		if self.root is None:
			return 0
		else:
			node_queue = [self.root]
			depth = 0
			while len(node_queue):
				q_len = len(node_queue)
				while q_len:
					node = node_queue.pop(0)
					q_len -= 1
					if node.lchild:
						node_queue.append(node.lchild)
					if node.rchild:
						node_queue.append(node.rchild)
				depth += 1
		return depth

	# 递归计算二叉树第k层结点个数
	def kth_node_count(self, node, k):
		"""二叉树第k层结点个数 = 二叉树左子树k-1层结点个数 + 二叉树右子树k-1层结点个数"""
		if not node or k <= 0:
			return 0
		if k== 1:
			return 1
		else:
			return self.kth_node_count(node.lchild, k-1) + self.kth_node_count(node.rchild, k-1)

	# 递归计算二叉树的叶子结点个数
	def leaf_count(self, node):
		"""叶子结点: 左右子结点均为None"""
		if not node:
			return 0
		if not node.lchild and not node.rchild:
			return 1
		return self.leaf_count(node.lchild) + self.leaf_count(node.rchild)

	# 判断两个二叉树是否相同
	def isSameTree(node1, node2):
		"""从根结点开始，递归向下判断值，左孩子，右孩子"""
		if node1 and node2:
			return (node1.elem == node2.elem) and \
					self.isSameTree(node1.lchild, node2.lchild) and \
					self.isSameTree(node1.rchild, node2.rchild)
		else:
			return False

	# 判断二叉树是否是二叉查找树
	def isBstTree(self, node):
		"""二叉树的中序遍历序列是递增的则是二叉查找树"""
		"""因为本代码实现的遍历没有存储遍历序列，所以暂不实现"""
		# # 假设inorder为中序遍历序列
		# isBST = True
		# while i < len(inorder) - 1:
		# 	if inorder[i] > inorder[i+1]:
		# 		isBST = False
		# 	i += 1
		# return isBST
		pass
		

def main():
	tree = BinaryTree()

	# 测试插入构造二叉树
	for i in range(10):
		tree.insert(i)

	# 测试层次遍历
	print("层次遍历: ")
	tree.bread_travel()
	print("\n")

	# 测试递归和非递归先序遍历
	print("递归前序遍历:")
	tree.preorder(tree.root)
	print("\t")
	print("非递归前序遍历:")
	tree.pre_order()
	print("\n")

	# 测试递归和非递归中序遍历
	print("递归中序遍历:")
	tree.inorder(tree.root)
	print("\t")
	print("非递归前序遍历:")
	tree.in_order()
	print("\n")

	# 测试递归和非递归后序遍历
	print("递归后序遍历:")
	tree.postorder(tree.root)
	print("\t")
	print("非递归后序遍历:")
	tree.post_order()
	print("\n")

	# 测试递归和非递归求树的高度
	print("递归求树的高度: ", tree.treeDepth(tree.root))
	print("非递归求树的高度: ", tree.tree_Depth())
	print("\t")

	# 测试求结点数量
	print("树的结点数量为: ", tree.nodeCount(tree.root))
	print("\t")

	# 测试第k层结点数计算方法
	for i in range(1,tree.treeDepth(tree.root)+1):
		print("第", i, "层结点数量为: ", tree.kth_node_count(tree.root, i))
	print("\t")

	# 测试求叶子结点个数
	print("树的叶子结点个数: ", tree.leaf_count(tree.root))

	
if __name__ == '__main__':
	main()