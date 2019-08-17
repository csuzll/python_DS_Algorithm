# 字典树(非二叉树)
# 下面建立纯英文字母的字典树，字母有26个，那么构建的trie树就是一个26叉树，每个结点包含26个子结点。

# 字典树结点类
class TrieNode:
    def __init__(self, a_char):
        self.char = a_char
        self.child = []
        self.is_leaf = False # 是否是叶子结点，即是否为一个完整单词的最后一个字母
        self.counter = 1 # 多少单词有这个共同前缀

# 纯英文字典树
class TrieTree:
    def __init__(self):
        self.root = TrieNode(None) # 根结点为一个无任何字符即是空的结点

    # 将一个单词加入到Trie树中
    def add_trie_word(self, word):
        """
            word为一个单词
        """
        curNode = self.root
        for ch in word: # 单词的每个字符
            found = False
            for node in curNode.child:
                if node.char == ch:
                    node.counter += 1
                    curNode = node
                    found = True
                    break
            if not found: # 未匹配前缀
                temp = TrieNode(ch)
                curNode.child.append(temp)
                curNode = temp
        curNode.is_leaf = True

    # 查找某个单词前缀是否在Trie树，并返回有多少个单词有这个共同前缀
    def search_trie_prefix(self,prefix):
        root = self.root
        if not root.child:
            return False,0
        for char in prefix:
            found=False
            for node in root.child:
                if node.char==char:
                    root=node
                    found=True
                    break
            if not found:
                return False,0
        return True, root.counter

trie_tree = TrieTree()
trie_tree.add_trie_word("hammer")
trie_tree.add_trie_word("ham")
trie_tree.add_trie_word("had")
print(trie_tree.search_trie_prefix("ha"))
print(trie_tree.search_trie_prefix("ham"))
print(trie_tree.search_trie_prefix("had"))
print(trie_tree.search_trie_prefix("b"))