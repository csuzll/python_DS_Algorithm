from stack import Stack

# 中缀表达式转换为前缀表达式
"""
要求：
输入：中缀表达式所有token用空格隔开，以便于分割。运算符只包括+，-，*，/，**，(，)。操作数只能为A~Z或者0~9
输出：前缀表达式字符串，各个token用空格隔开。

1、 构建一个空操作符栈opstack用于保存运算符，创建一个空list代表前缀表达式
2、 将中缀表达式转换为list。通过split()。
3、 从右到左扫描中缀list的token
    (1)如果token为操作数，则添加到前缀list末尾；
    (2)如果token为右括号，则压入栈中；
    (3)如果token为左括号，将栈中的元素弹出，直到遇到右括号。将弹出的运算符不包括右括号添加到前缀list末尾。
    (4)如果token为+，-，*，/, **。将其压入栈中，但是先要判断栈顶上的操作符的优先级是否大于当前token，如果是则将栈顶运算符弹出添加到前缀list末尾。直至栈顶小于等于当前。
4、 当输入表达式已经被完全处理，再检查opstack。仍然在栈上的任何运算符都可以删除并加到前缀list的末尾。
5、 将前缀list反转

异常处理: 括号不平衡
"""

# 前缀表达式求值
"""
要求：输入的前缀表达式所有token用空格隔开，以便于分割。运算符只包括+，-，*，/，**。操作数只能为0~9
返回：一个值。

算法思路：
1、 创建一个空操作数栈operandStack。
2、 将前缀表达式转换为list，通过split()。
3、 从右至左遍历前缀表达式：
    (1)如果token是操作数，则压入栈中。
    (2)如果token是操作符，则弹出栈中的最近的两个操作数（在这里检查操作数是否大于等于2，否则输出错误信息）。第一次弹出的作为第1操作数，第二次弹出的作为第2操作数。然后将他们之间的运算结果压入栈中。
    (3)如果都不是，则输出错误信息。
4、 当遍历完输入表达式后，检查operandStack是否等于1。等于进入第5步，不等于则输出错误信息。
5、 栈中唯一剩下的value就是表达式计算结果。

异常处理：操作符和操作数的检查是否缺少。操作符和操作数是否符合输入要求。
"""

# 中缀表达式转为前缀表达式
def infixToprefix(infixexpr):
    # prec字典保存操作符的优先级
    prec = {"**":4, "*":3, "/":3, "+":2, "-":2, "(":1, ")":1}
    # 操作符栈
    opstack = Stack()
    # 中缀表达式转换为list
    tokenlist = infixexpr.split()
    # 前缀表达式list
    prefixlist = []
    # 栈中剩余的右括号个数
    right_p_remain = 0

    # 从右向左扫描
    for token in reversed(tokenlist):
        # 如果token是操作数，则将其添加到前缀list的末尾
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixlist.append(token)
        # 如果token是右括号，将其压入操作符栈中，栈中右括号数+1
        elif token == ")":
            opstack.push(token)
            right_p_remain += 1
        # 如果token是左括号，栈中右括号数-1，进行异常检测，正常则将栈中的元素弹出并加入前缀list末尾，直到删除右括号。
        elif token == "(":
            right_p_remain -= 1
            if right_p_remain < 0:
                raise Exception("parenthesis are not balance, please check!")
            while opstack.peek() != ")":
                prefixlist.append(opstack.pop())
            opstack.pop()
        # 如果token是操作符，将其压入栈。但是，首先删除已经在栈中且具有更高优先级的任何运算符，
        # 并将他们添加到前缀list末尾
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] > prec[token]):
                prefixlist.append(opstack.pop())
            opstack.push(token)
    # 检查栈中剩余右括号数
    if right_p_remain != 0 :
        raise Exception("parenthesis are not balance, please check!")
    # 当输入表达式被完全处理后，检查栈，若有剩余，则pop并添加到前缀列表的末尾
    while not opstack.isEmpty():
        prefixlist.append(opstack.pop())
    # 反转序列
    prefixlist.reverse()
    return " ".join(prefixlist)

# 前缀表达式求值
def prefixEval(prefixexpr):
    # 操作数栈
    operandStack = Stack()
    # 前缀表达式转换为list
    tokenList = prefixexpr.split()

    for token in reversed(tokenList):
        if token in "0123456789":
            operandStack.push(int(token)) # 压入栈时，记得把操作数转换为数字类型
        elif token in "+-*/" or token == "**":
            # token是个操作符，需要出栈两个操作数，先检查操作数够不够。然后再将结果压入栈。
            if operandStack.size() < 2:
                raise Exception("not enough operand, please check!")
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        else:
            # token不符合输入要求
            raise Exception("too much operand, please check!")
    if operandStack.size() != 1:
        pass
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "**":
        return op1 ** op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    instr = "1 + ( ( 2 + 3 ) * 4 ) - 5"
    prestr = infixToprefix(instr)
    prestr_result = prefixEval(prestr)
    print(prestr)
    print(prestr_result)