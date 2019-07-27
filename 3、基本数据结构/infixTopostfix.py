from stack import Stack

# 中缀表达式转换为后缀表达式
"""
要求：
输入：中缀表达式所有token用空格隔开，以便于分割。运算符只包括+，-，*，/，**，(，)。操作数只能为A~Z或者0~9
输出：后缀表达式字符串，各个token用空格隔开。

1、 构建一个空操作符栈opstack用于保存运算符，创建一个空字符串代表后缀表达式
2、 将前缀表达式转换为list。通过split()。
3、 从左到右扫描前缀list的token
    (1)如果token为操作数，则添加到后缀字符串末尾；
    (2)如果token为左括号，则压入栈中
    (3)如果token为右括号，将栈中的元素弹出，知道遇到左操作符。将弹出的运算符不包括左括号添加到后缀字符串末尾。
    (4)如果token为+，-，*，/。将其压入栈中，但是先要判断栈中最顶上的操作符的优先级是否大于或等于当前token，如果是则将栈中运算符弹出添加到字符串末尾。
4、 当输入表达式已经被完全处理，再检查opstack。仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。
异常处理: 括号不平衡（可在这里添加）
"""
def infixTopostfix(infixexpr):

    # prec字典保存操作符的优先级
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    # 存储操作符的栈
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()
    # 栈中剩余的左括号的个数
    left_p_remain = 0

    for token in tokenlist:
        # 将操作数定义为任何大写字符和数字
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == "(":
            opstack.push(token)
            left_p_remain += 1
        elif token == ")":
            left_p_remain -= 1
            if left_p_remain < 0:
                raise Exception("parenthesis are not balance, please check!")
            topToken = opstack.pop()
            while topToken!= "(":
                postfixlist.append(topToken)
                topToken = opstack.pop()
        else:
            while (not opstack.isEmpty() and (prec[opstack.peek()] >= prec[token])):
                postfixlist.append(opstack.pop())
            opstack.push(token)
    if left_p_remain != 0:
        raise Exception("parenthesis are not balance, please check!")
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())

    # " ".join(iterable)是指在可迭代对象中插入空格
    return " ".join(postfixlist)

print(infixTopostfix("A * B + C * D"))  #  A B * C D * +
print(infixTopostfix("( A + B ) * C - ( D - E ) * ( F + G )"))  #  A B + C * D E - F G + * -
print(infixTopostfix("5 * 3 ** ( 4 - 2 )")) # 5 3 4 2 - ** *
# print(infixTopostfix("( A + B ) * C - ( D - E ) ) * ( F + G)")) # 出错
print(infixTopostfix("( 1 + 3 ) / ( ( 3 - 8 ) * 9 )")) # 1 3 + 3 8 - 9 * /

print(infixTopostfix("( A + B ) * ( C + D ) * ( E + F )"))
print(infixTopostfix("A + ( ( B + C ) * ( D + E ) )"))
print(infixTopostfix("A * B * C * D + E + F"))