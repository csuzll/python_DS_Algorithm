"""对比list和dict的del 操作"""
from timeit import Timer

def test10():
    alist = list(range(1000))

    for i in range(1000):
        del alist[0]

def test11():
    d = dict(zip(list(range(1000)), list(range(1000,2000))))
    for i in range(1000):
        del d[i]

t10 = Timer("test10()", "from __main__ import test10")
print("list del item:", t10.timeit(number=1000), "milliseconds")
t11 = Timer("test11()", "from __main__ import test11")
print("dict del item:", t11.timeit(number=1000), "milliseconds")