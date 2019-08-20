 # 顺序查找

 # 实现方法一: 在原始list中进行顺序查找，返回是否找到
 # 该算法为O(n)，len()仅为O(1)
def sequentialSearch(alist, item):
    index = 0 # 下标
    found = False # 找到标志

    while index < len(alist) and not found:
        if alist[index] == item:
            found = True
        else:
            index += 1
    return found

# 已排序(升序)的list中进行顺序查找
# 当找到的数已经大于了要查找的数，则可以结束循环停止了。
# 该算法依然为O(n)
def orderedSequentialSearch2(alist, item):
    index = 0
    found = False
    stop = False

    while index < len(alist) and not found and not stop:
        if alist[index] == item:
            found = True
        else:
            if alist[index] > item:
                stop = True
            else:
                index += 1
    return found

if __name__ == '__main__':
    testlist1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist1, 3))
    print(sequentialSearch(testlist1, 13))

    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(orderedSequentialSearch2(testlist2, 3))
    print(orderedSequentialSearch2(testlist2, 13))