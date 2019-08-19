# from __future__ import division

# 求两个数的最大公约数
def gcd(m, n):
    while (n!=0):
        rem = m % n
        m = n
        n = rem
    return m

class Fraction:

    """处理分数的类"""

    def __init__(self, top, bottom):

        # 检查分子分母是否都是整数
        if (not isinstance(top, int) or not isinstance(bottom, int)):
            raise ValueError("top and bottom of Fraction is not int type!")
        if (bottom == 0):
            raise ZeroDivisionError("bottom of Fraction can't be zero!")

        # 初始化时直接约简
        common = gcd(top,bottom)
        self.num = top // common # 分子
        self.den = bottom // common # 分母

    # 能让print()显示分数类型的形式
    def __str__(self):
        # 分数为0直接显示0吧
        if (self.num == 0):
            return str(0)
        else:
            return str(self.num) + "/" + str(self.den)

    # 也可以调用类方法按要求显示分数数据
    def show(self):
        print(self.num, "/", self.den)

    # 获取分子
    def getNum(self):
        return self.num

    # 获取分母
    def getDen(self):
        return self.den 

    # 加法
    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    # 减法
    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    # 乘法
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    # 除法
    def __truediv__(self, other):
        if (other.num == 0):
            raise ZeroDivisionError("the divisor cannot be zeor!")
        else:
            newnum = self.num * other.den
            newden = self.den * other.num

            return Fraction(newnum, newden)

    # 相等
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum

    # 大于
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum

    # 大于等于
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum >= secondnum

    # 小于
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum < secondnum

    # 小于等于
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum <= secondnum

    # 不等于
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum != secondnum

    # 分数和int型数据的加法
    def __radd__(self, other_int):
        """会先调用__add__()，如果返回NotImplemented，则调用__radd__()"""
        newnum = self.num + self.den * other_int

        return Fraction(newnum, self.den)

    # "+="类型的加法
    def __iadd__(self, other):
        """a = iadd(a,b) 等价于 a += b"""
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    # __repr__是用于输出更多的关于对象的信息的，而__str__是为了print好看的
    def __repr__(self):
        return "num: {}, " "den: {}".format(self.num, self.den)

# 测试
def main():
    # 测试非整数
    try:
        assert Fraction(0.1, 2)
    except ValueError as e:
        print("Int number test is ok.")

    # 测试分母不能为0
    try:
        assert Fraction(2, 0), "den is zero"
    except ZeroDivisionError as e:
        print("zero denominator test is ok.")

    # 测试分子为0的输出
    print(Fraction(0, 1))  # 输出为"0"

    # 测试分子分母为均为正整数
    print(Fraction(2, 4)) # 输出"1/2"
    # 测试分子分母均为负整数
    print(Fraction(-2, -4)) # 输出"1/2"
    # 测试分子为负整数，分母为正整数
    print(Fraction(-2, 4))  # 输出"-1/2"
    # 测试分子为正整数，分母为负整数
    print(Fraction(2, -4))  # 输出"-1/2"，负号不在分母前

    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = Fraction(2, 4)

    # 以下测试仅支持同类实例
    # 测试"__add__"
    print(x + y) # 输出"7/6"
    print(x - y) # 输出"-1/6"
    print(x * y) # 输出"-1/3"
    print(x / y) # 输出"3/4"
    print(x == y) # False
    print(x != y) # True
    print(x == z) # True
    print(x < y)  # True
    print(x > y)  # False
    print(x <= y) # True
    print(x >= y) # False
    print(x <= z) # True
    print(x >= z) # True
    x += y
    print(x) # x变为了"7/6"

    # 分数类型和不同类型的相加
    # 测试"__radd__()"
    print(1 + z) # 输出"3/2"，分数必须在其他类型之后
    # print(z + 1) 会出错

    # 测试"__repr__()"
    print(repr(z))

if __name__ == '__main__':
    main()

