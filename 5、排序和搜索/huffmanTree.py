# 哈夫曼树

# 构建字符频率哈夫曼树

from PriorityQueue import PriorityQueue

# 哈夫曼树结点
class HaffumanNode:
    def __init__(self, value=None, weight=None, lchild=None, rchild=None):
        """
            value: 元素
            weight: 元素的权重
            lchild: 左孩子结点
            rchild: 右孩子结点
        """
        self.value = value
        self.weight = weight
        self.lchild = lchild
        self.rchild = rchild

    # 判断是否为叶子结点
    def is_leaf(self):
        return not self.leftchild and not self.rightchild

    # 用于两个对象间比较大小
    def __lt__(self, other):
        return self.weight < other.weight

# 根据哈夫曼树获得哈夫曼编码
def getHaffumanCode(root, code, code_dict1, code_dict2):
    pass


# 哈夫曼树
class HaffumanTree(PriorityQueue):
    