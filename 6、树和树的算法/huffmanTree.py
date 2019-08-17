# 哈夫曼树

# 构建字符频率(权重)哈夫曼树，实现编码和解码

# 1、统计各个字符在字符串中出现的次数，即计算优先度或权重
def count_frequency(text):
    d = {}
    for c in text: # text中的单个字符
        if not c in d: # 关键字c在d字典中未出现过
            d[c] = 1
        else:
            d[c] += 1

    # 将d字典中的元素按关键字对应的值从小到大排序
    return sorted(d.items(), key=lambda x: x[1])

# 2、哈夫曼树结点类
class HaffumanNode:
    def __init__(self, data, lchild=None, rchild=None):
        """
            data: 结点元素（含元素值和优先度），例如("a", 1)
            lchild: 左孩子结点
            rchild: 右孩子结点
        """
        self.value = data[0] # 元素的值（统计字符）
        self.weight = data[1] # 元素的权重或者优先度（字符出现的频率）
        self.lchild = lchild
        self.rchild = rchild
        self.code = "" # 结点的编码

# 3、创建结点队列类
class nodeQueue:
    def __init__(self, codes):
        self.que = self._creatnodeQ(codes) # 结点队列
        self.size = len(self.que) # 结点队列大小

    # 私有方法: 创建树结点队列
    def _creatnodeQ(self, codes):
        q = []
        for code in codes:
            q.append(HaffumanNode(code))
        return q

    # 为队列添加结点元素，并保证优先度从小到大排列
    def addNode(self, node):
        if self.size == 0: # 列表为空
            self.que = [node]
        else:
            if node.weight >= self.que[-1].weight: # 新结点的权重大于列表最后一个元素的权重
                self.que = self.que + [node]
            else:
                i = 0 
                while i < self.size:
                    if self.que[i].weight > node.weight:
                        self.que = self.que[:i] + [node] + self.que[i:]
                        break
                    i = i + 1
        self.size += 1

    # 弹出队列首部的结点
    def popNode(self):
        self.size -= 1
        return self.que.pop(0)

# 4、创建哈夫曼树
def HuffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.popNode() # 最小权重结点1
        node2 = nodeQ.popNode() # 最小权重结点2

        # 由node1和node2组成的新树
        r = HaffumanNode([None, node1.weight + node2.weight]) # 此新树的根结点的权重为两个结点的和
        r.lchild = node1
        r.rchild = node2

        # 将这个新树加入到哈夫曼结点队列中
        nodeQ.addNode(r)

    # 最后哈夫曼结点队列只剩下1个结点，即为哈夫曼树
    return nodeQ.popNode()

codeDic1 = {}
codeDic2 = {}

# 5、由哈夫曼树得到哈夫曼编码表
def HuffmanCodeDic(tree, x = ""):
    global codeDic, codeList
    if tree:
        HuffmanCodeDic(tree.lchild, x + "0")
        tree.code += x
        if tree.value:
            codeDic2[tree.code] = tree.value
            codeDic1[tree.value] = tree.code
        HuffmanCodeDic(tree.rchild, x + "1")

# 6、字符串编码
def TransEncode(string):
    global codeDic1
    transcode = ""
    for c in string:
        transcode += codeDic1[c]
    return transcode

# 7、字符串解码
def TransDecode(StringCode):
    global codeDic2
    code = ""
    ans = ""
    for ch in StringCode:
        code += ch
        if code in codeDic2:
            ans += codeDic2[code]
            code = ""
    return ans


strss = "abcdabcdeg"
dict1 = count_frequency(strss)
print(dict1)

t = nodeQueue(dict1)
a = t.que
for i in range(t.size):
    print(a[i].value, a[i].weight)

tree = HuffmanTree(t)
print(tree.value, tree.weight)
print(tree.lchild.value, tree.lchild.weight)
print(tree.rchild.value, tree.rchild.weight)
print(tree.lchild.lchild.value, tree.lchild.lchild.weight)
print(tree.lchild.rchild.value, tree.lchild.rchild.weight)
print(tree.rchild.lchild.value, tree.rchild.lchild.weight)
print(tree.rchild.rchild.value, tree.rchild.rchild.weight)
print(tree.rchild.lchild.lchild.value, tree.rchild.lchild.lchild.weight)
print(tree.rchild.lchild.rchild.value, tree.rchild.lchild.rchild.weight)
print(tree.rchild.rchild.lchild.value, tree.rchild.rchild.lchild.weight)
print(tree.rchild.rchild.rchild.value, tree.rchild.rchild.rchild.weight)

HuffmanCodeDic(tree)
print(codeDic1, codeDic2)

a = TransEncode(strss)
print(a)
aa = TransDecode(a)
print(aa)
print(strss == aa)