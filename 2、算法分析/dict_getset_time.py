from timeit import Timer

"""证明dict的get()和set()是O(1)"""
# 先认为dict的遍历是O(n)

def test7():
    d = dict(zip(list(range(1000)), list(range(1000, 2000))))
    for i in range(1000):
        d[i] = 1

def test8():
    d = dict(zip(list(range(1000)), list(range(1000, 2000))))
    for i in range(1000):
        v = d[i]

def test9():
    d = dict(zip(list(range(1000)), list(range(1000, 2000))))
    for i in range(1000):
        for one in d:
            pass

t7 = Timer("test7()", "from __main__ import test7")
print("dict set item: ", t7.timeit(number=1000), "milliseconds")
t8 = Timer("test8()", "from __main__ import test8")
print("dict get item: ", t8.timeit(number=1000), "milliseconds")
t9 = Timer("test9()", "from __main__ import test9")
print("dict iteration: ", t9.timeit(number=1000), "milliseconds")