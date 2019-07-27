# 比较python内置的list和实现的无序链表
from unorderlist2 import UnorderedList

def list_test():
    l = []
    for i in range(1000):
        l.append(i)
    for i in range(1000):
        l.pop()

def unorderlist_test():
    ul = UnorderedList()
    for i in range(1000):
        ul.append(i)
    for i in range(1000):
        ul.pop() 

from timeit import Timer
t9 = Timer("list_test()", "from __main__ import list_test")
print("list :",t9.timeit(number=100), "milliseconds")
t10 = Timer("unorderlist_test()", "from __main__ import unorderlist_test")
print("unorded list :",t10.timeit(number=100), "milliseconds")