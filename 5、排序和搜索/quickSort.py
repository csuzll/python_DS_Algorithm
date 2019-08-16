# 快速排序
"""

快速排序通常明显比同为Ο(NlogN)的其他算法更快，因此常被采用。
使用枢纽值将列表划分为两部分，一部分小于枢纽值，另一部分大于枢纽值，
递归进行。

时间复杂度: 平均O(NlogN)，最好O(NlogN)，最坏O(N^2)
空间复杂度: O(logn)到O(n)

不稳定
"""

# 快速排序，pivot选择为待排序列表中的第一项
# 这种写法时间复杂度为O(logN)
def quickSort(alist, first=0, last=None):
    last = len(alist)-1 if last == None else last
    if first < last:
        splitpoint = partition(alist, first, last)
        # 分治
        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)

def partition(alist, first, last):
    pivotvalue = alist[first]  # 基准值
    leftmark = first+1 # 左界    
    rightmark = last # 右界

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
    # 此时右标记为基准值应该插入的位置，交换右标记与基准值
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark # 返回分割点位置

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


# # 快速排序，pivot选择为待排序列表中的中间位置的值（感觉实现得不太好）
# def quickSort2(alist, first, last):
#     if first < last:
#         splitpoint = partition2(alist, first, last)
#         # 递归子序列
#         quickSort2(alist, first, splitpoint-1)
#         quickSort2(alist, splitpoint+1, last)

# def partition2(alist, first, last):
#     # 中间元素作为基准值
#     pivot = (first + last) // 2
#     pivotvalue = alist[pivot]

#     # 使用双引用向中间靠拢
#     leftmark = first
#     rightmark = last

#     done = False
#     print("pivotvalue: ", pivotvalue)
#     while not done:
#         while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1
#         while rightmark >= leftmark and alist[rightmark] >= pivotvalue and rightmark > first:
#             rightmark = rightmark - 1

#         if rightmark < leftmark or rightmark == first:
#             done = True
#         else:
#             alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

#     alist[pivot], alist[rightmark] = alist[rightmark], alist[pivot]
#     return leftmark # 返回左标记值

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort2(alist, 0, len(alist)-1)
# print(alist)


# 使用三位取中设置枢纽值实现快速排序
# 此代码实现空间复杂度较高（需要改进），时间复杂度为O(NlogN)
def quickSort3(alist):
    if len(alist) <= 1:
        return alist
    else:
        threelist = [alist[0], alist[-1], alist[len(alist) // 2]] # 第一，最末，中间元素组成的列表
        pivotvalue = sorted(threelist)[1]  # 3个数的中位数，枢纽值
        index = alist.index(pivotvalue)  # 确定枢纽值在原列表中的位置

        left = quickSort3([l for l in (alist[:index] + alist[index+1:]) if l <= pivotvalue])
        right = quickSort3([r for r in (alist[:index] + alist[index+1:]) if r > pivotvalue])

        return left+[pivotvalue]+right

alist = [54,26,93,17,77,31,44,55,20]
print(quickSort3(alist))

# 三位取中(三路快排)的第二种实现
def quickSort4(alist, first=0, last=None):
    last = len(alist)-1 if last == None else last

    if first >= last:
        return None

    #  从alist[first],alist[mid],alist[last]三个中挑选中间值，并将其移动到alist[first]
    mid = (first + last) // 2
    if alist[first] > alist[last]:
        alist[first], alist[last] = alist[last], alist[first]
    if alist[mid] < alist[last]:
        alist[mid], alist[last] = alist[last], alist[mid]
    if alist[first] < alist[mid]:
        alist[first], alist[mid] = alist[mid], alist[first]

    pivotvalue = alist[first]  # 基准值
    leftmark = first+1 # 左界    
    rightmark = last # 右界

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
    # 此时右标记为基准值应该插入的位置，交换右标记与基准值
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    quickSort(alist, first, rightmark-1)
    quickSort(alist, rightmark+1, last)

alist = [54,26,93,17,77,31,44,55,20]
quickSort4(alist)
print(alist)


# 三路快排 +  插入排序
# 可以设定当列表数小于某个值的时候使用插入排序，其他情况使用快速排序（当排序数组较小时，插入排序的效率要高于快速排序）
