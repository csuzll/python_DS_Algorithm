# 快速排序，pivot选择为待排序列表中的第一项
def quickSort(alist, first, last):
    """
    first: 默认应该输入0
    last: 默认应为列表长度-1
    """
    if first < last:
        splitpoint = partition(alist, first, last)
        # 分治
        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)

def partition(alist, first, last):
    pivotvalue = alist[first]  # 基准值
    leftmark = first+1 # 左标记    
    rightmark = last # 右标记

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue: # 向右移动左标记直到超过右标记或找到大于基准数的项
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark: # 向左移动右标记直到超过左标记或找到小于基准数的项
            rightmark = rightmark -1

        if rightmark < leftmark: # 左标记小于右标记，结束
            done = True
        else: # 否则，交换左右标记的指向的值值
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    # 交换右标记与基准值
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark # 返回分割点位置

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist, 0, len(alist)-1)
print(alist)


# 快速排序，pivot选择为待排序列表中的中间位置的值
def quickSort2(alist, first, last):
    if first < last:
        splitpoint = partition2(alist, first, last)
        # 递归子序列
        quickSort2(alist, first, splitpoint-1)
        quickSort2(alist, splitpoint+1, last)

def partition2(alist, first, last):
    # 中间元素作为基准值
    pivot = (first + last) // 2
    pivotvalue = alist[pivot]

    # 使用双引用向中间靠拢
    leftmark = first
    rightmark = last

    done = False
    print("pivotvalue: ", pivotvalue)
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue and rightmark > first:
            rightmark = rightmark - 1

        if rightmark < leftmark or rightmark == first:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[pivot], alist[rightmark] = alist[rightmark], alist[pivot]
    return leftmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort2(alist, 0, len(alist)-1)
print(alist)




