"""4种从0生成list的操作"""
import timeit
import random

# for循环和“+”
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

# for循环和append
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# 列表表达式
def test3():
    l = [i for i in range(1000)]

# 列表构造函数包装的范围函数
def test4():
    l = list(range(1000))


# 测试4种方法所用的时间
t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("apped ",t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")


"""测试在不同大小的列表中删除最后一个元素和第一个元素所用的时间"""
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")
print("pop(0)   pop()")
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number = 1000)
    x = list(range(i))
    pz = popzero.timeit(number = 1000)
    print("%15.5f, %15.5f" % (pz, pt))


# 测试在列表和字典中查找的时间差异
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number = 1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))