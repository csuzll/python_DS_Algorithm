# 字典树(非二叉树)

class TrieNode:
    def __init__(self, a_char):
        self.char = a_char
        self.child = []
        self.is_leaf = False # 是否是叶子结点，即是否为一个完整单词的最后一个字母
        self.counter = 1 # 多少单词有这个共同前缀

class TrieTree:
    def __init__(self):
        self.root = TrieNode(None) # 根结点为一个无任何字符即是空的结点


    # 将一个单词加入到Trie树中
    def add_word(self, word):
        """
            word为一个单词
        """
        curNode = self.root
        for ch in word: # 单词的每个字符
            found = False
            for node in curNode.child:
                if node.char = ch:
                    node.counter += 1
                    curNode = node
                    found = True
                    break
            if not found: # 未匹配前缀
                temp = TrieNode(ch)
                curNode.child.append(temp)
                curNode = temp
        # 当前结点可能不再是root
        curNode.is_leaf = True

