"""证明列表的索引操作时间复杂度为O(1)"""
# 假设list的pop(0)是O(n)是已知条件

from timeit import Timer

def test5():
    alist = list(range(1000))
    for i in range(1000):
        alist[i] = 1

def test6():
    alist = list(range(1000))
    for i in range(1000):
        alist.pop(0)

t5 = Timer("test5()", "from __main__ import test5")
print("list index operation: ", t5.timeit(number=10), "milliseconds")
t6 = Timer("test6()", "from __main__ import test6")
print("list pop(0): ", t6.timeit(number=10), "milliseconds")