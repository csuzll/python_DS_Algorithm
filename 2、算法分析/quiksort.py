# python 实现快速排序算法

# solution1
def qsort1(alist):
    """Quicksort using list comprehensions"""
    if alist == []:
        return []
    else:
        pivot = alist[0]
        lesser = qsort1([x for x in alist[1:] if x < pivot])
        greater = qsort1([x for x in alist[1:] if x >= pivot])
        return lesser + [pivot] + greater

# solution2
def qsort2(alist):
    """Quicksort using a partitoning function"""
    if alist == []:
        return []
    else:
        pivot = alist[0]
        lesser, equal, greater = partition2(alist[1:], [], [pivot], [])
        return qsort2(lesser) + equal + qsort2(greater)

def partition2(alist, l, e, g):
    while alist != []:
        head = alist.pop(0)
        if head < e[0]:
            l = l + [head]
        elif head > e[0]:
            g = g + [head]
        else:
            e = e + [head] 
    return (l, e, g)

# solution3
def qsort3(alist, left, right):
    if alist == []:
        return []
    else:
        pivot = 0
        if left < right:
            pivot = partition3(alist, left, right)
            qsort3(alist, left, pivot-1)
            qsort3(alist, pivot+1, right)
        return alist

def partition3(alist, left, right):
    key = alist[left]

    while left < right:
        while left < right and alist[right] >= key:
            right = right -1
        alist[left] = alist[right]
        while left < right and alist[left] <= key:
            left = left + 1
        alist[right] = alist[left]
    alist[left] = key

    return left

if __name__ == '__main__':
    list1 = [65,58,95,10,57,65,13,106,78,23,85]
    list2 = [65,58,95,10,57,65,13,106,78,23,85]
    list3 = [65,58,95,10,57,65,13,106,78,23,85]
    print(list1)
    print(qsort1(list1))
    print(qsort2(list2))
    print(qsort3(list3, 0, len(list3)-1))