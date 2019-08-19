"""
实现在数列中查找最小值，用两种方法实现，一种算法时间复杂度为O(N2)，另一种算法时间复杂度为O(N)
"""
import time
from random import randrange

# O(N2)
def findMin1(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issamllest = False
            if issmallest:
                overallmin = i
    return overallmin

# O(N)
def findMin2(alist):
    overallmin = alist[0]
    for num in alist:
        if num < overallmin:
            overallmin = num
    return overallmin

if __name__ == '__main__':
    for listSize in range(1000,10001,1000):
        alist = [randrange(100000) for x in range(listSize)]
        start = time.time()
        print(findMin1(alist))
        end = time.time()
        print("size: %d time: %f" % (listSize, end-start))

    for listSize2 in range(1000,10001,1000):
        alist = [randrange(100000) for x in range(listSize2)]
        start = time.time()
        print(findMin2(alist))
        end = time.time()
        print("size: %d time: %f" % (listSize2, end-start))