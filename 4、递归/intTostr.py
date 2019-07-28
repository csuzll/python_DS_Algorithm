# 将整数转换为任意进制字符串

# 递归方法：
def int2str(number, base):
    convstring = "0123456789ABCDEF"
    if number < base:
        return convstring[number]
    else:
        single_num = number % base
        number = number // base
        return int2str(number, base) + convstring[single_num]

print(int2str(1453, base=16))


# 非递归方法
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

rStack = Stack()

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))

# 上面这个例子让我们了解Python如何实现一个递归函数调用。
# 当在Python中调用函数时，会分配一个栈来处理函数的局部变量。当函数返回时，返回值留在栈的顶部，以供调用函数访问。
# Stack Frames还为函数使用的变量提供了一个作用域。 即使我们重复地调用相同的函数，每次调用都会为函数本地的变量创建一个新的作用域。