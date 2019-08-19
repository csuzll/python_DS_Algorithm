from stack import Stack

# 后缀表达式求值
"""
要求：输入的后缀表达式所有token用空格隔开，以便于分割。运算符只包括+，-，*，/，**。操作数只能为0~9
返回：一个值。

算法思路：
1、 创建一个空操作数栈operandStack。
2、 将后缀表达式转换为list，通过split().
3、 从左至右遍历后缀表达式：
    (1)如果token是操作数，则压入栈中。
    (2)如果token是操作符，则弹出栈中的最近的两个操作数（在这里检查操作数是否大于等于2，否则输出错误信息）。第一次弹出的作为第二操作数，第二次弹出的作为第一操作数。然后将他们之间的运算结果压入栈中。
    (3)如果都不是，则输出错误信息。
4、 当遍历完输入表达式后，检查operandStack是否等于1。等于进入第5步，不等于则输出错误信息。
5、 栈中唯一剩下的value就是表达式计算结果。

异常处理：操作符和操作数的检查是否缺少。操作符合操作数符不符合输入要求。
"""
def postfixEval(postfixexpr):
    operandStack = Stack()
    tokenList = postfixexpr.split()

    for token in tokenList:
        # 操作数定义为0~9
        if token in "0123456789":
            operandStack.push(int(token))
        elif token in "+-*/" or token == "**":
            # token是个操作符，需要出栈两个操作数，提前检查操作数够不够
            if operandStack.size() < 2:
                raise Exception("not enough operand, please check!")
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        else:
            # token不符合输入要求
            raise Exception("input are not in '0123456789' or not in '+-*/' or not equal '**'")
    if operandStack.size() != 1:
        raise Exception("too much operand, please check!")
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2s
    elif op == "/":
        return op1 / op2
    elif op == "**":
        return op1 ** op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    print(postfixEval('7 8 + 3 2 + /')) # 3.0
    # print(postfixEval('7 8 + 3 2 + / -')) # 出错
    print(postfixEval("1 3 + 3 8 - 9 * /"))
    print(postfixEval("11 3 + 3 8 - 9 * /")) # 出错