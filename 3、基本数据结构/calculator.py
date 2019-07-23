# 将中缀转换为后缀及后缀计算合在一起，形成一个计算器
from stack import Stack

class Calculator:
    """支持0-9的加减乘除幂运算的简单计算器"""
    def __init__(self):
        pass

    def calc(self, infix):
        postfix = self.infixTopostfix(infix)
        return self.postfixEval(postfix)

    def infixTopostfix(self, infixexpr):

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

        return " ".join(postfixlist)

    def postfixEval(self, postfixexpr):
        operandStack = Stack()
        tokenList = postfixexpr.split()

        for token in tokenList:
            # 操作数定义为0~9
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                # token是个操作符，需要出栈两个操作数，提前检查操作数够不够
                if operandStack.size() < 2:
                    raise Exception("not enough operand, please check!")
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = self.doMath(token, operand1, operand2)
                operandStack.push(result)
        if operandStack.size() != 1:
            raise Exception("too much operand, please check!")

        return operandStack.pop()

    def doMath(slef, op, op1, op2):
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

cal = Calculator()
expr = "( 1 + 3 ) / ( ( 3 - 8 ) * 9 )"
print(cal.calc(expr)) #  -0.08888888888888889