# 实现一个栈，利用列表实现，添加和删除在list的末端

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

# # 测试
# s = Stack()
# print(s.isEmpty()) # True
# s.push("dog") # ["dog"]
# print(s.peek())  # dog
# s.push(True)  # ["dog", True]
# print(s.size()) # 2
# print(s.isEmpty()) # False
# s.push(8.4) # ["dog", True, 8.4]
# print(s.pop()) # 8.4
# print(s.pop()) # True
# print(s.size()) # 1


# # 实现一个栈，利用列表实现，添加和删除在list的首端。
# class Stack:

#     def __init__(self):
#         self.items = []

#     # 判断是否为空
#     def isEmpty(self):
#         return self.items == []

#     # 添加item
#     def push(self, item):
#         self.items.insert(0, item)

#     # 删除item
#     def pop(self):
#         return self.items.pop(0)

#     # 获取top端的item
#     def peek(self):
#         return self.items[0]

#     # 获取栈中元素个数
#     def size(self):
#         return len(self.items)

# # 测试 
# s = Stack()
# s.push('hello') # ["hello"]
# s.push('true') # ["true", "hello"]
# print(s.pop()) # "true"


"""
选择list[0]作为top还是base，在时间复杂度上有着截然不同的区别。因为list的append和pop()操作都
只需要 O(1)的时间复杂度，但insert(0)和pop(0)都需要 O(n)的复杂度。
"""


# 使用stack实现字符串反转
def revstring(mystr):
    s = Stack()
    revstr = ""

    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        revstr = revstr + s.pop()
    return revstr

# 测试
assert revstring("apple") == "elppa", "apple Error"
assert revstring("x") == "x", "x Error"
assert revstring("1234567890") == "0987654321", "error"
