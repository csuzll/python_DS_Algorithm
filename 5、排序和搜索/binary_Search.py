# 二分查找(已排好序(升序)的列表)

# 实现方法一: 迭代思想，O(log n)，比较次数
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

# 实现方法二: 这个使用了分治的思想，所以可以用递归实现
# 利用了切片操作O(k)，则该算法时间复杂度可能不在对数时间log(n)内。
def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint+1:], item)

# 实现方法三: 改进递归的方法,不使用切片。这里没找到返回None，找到返回True
def binarySearch3(alist, item, first=0, last=None):
    last = len(alist) if last==None else last # 让下面传上来的元素的个数不改变初始的元素个数
    midpoint = (first + last) // 2
    if first <= last:
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] > item:
            return binarySearch3(alist, item, first=first, last=midpoint-1)
        else:
            return binarySearch3(alist, item, first=midpoint+1, last=last)
    else:
        return False

if __name__ == '__main__':

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))

    print(binarySearch2(testlist, 3))
    print(binarySearch2(testlist, 13))
    
    print(binarySearch3(testlist, 3))
    print(binarySearch3(testlist, 13))