from stack import Stack

# 括号平衡性检查(单种括号)
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    # 从头开始检查
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(": # 左括号则入栈
            s.push(symbol)
        else:
            if s.isEmpty(): # 遇到右括号但是栈是空的
                balanced = False
            else: # 遇到右括号就弹出一个左括号
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
        
# 符号平衡性检查(包括括号，中括号，花括号)
def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{": # 左括号、左中括号、左花括号则入栈
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                # 弹出栈的top元素与此时的symbol比较
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    # balanced为True，且栈为空，则返回匹配True
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(a_open, a_close):
    opens = "([{"
    closers = ")]}"
    # 按其位置的index进行匹配
    return opens.index(a_open) == closers.index(a_close)

if __name__ == '__main__':
    print(parChecker('((()))')) # True
    print(parChecker('(()')) # False

    print(parChecker2('{{([][])}()}')) # True
    print(parChecker2('[{()]')) # False





