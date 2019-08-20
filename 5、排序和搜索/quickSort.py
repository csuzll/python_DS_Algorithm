# 快速排序
"""

快速排序通常明显比同为Ο(NlogN)的其他算法更快，因此常被采用。
使用枢纽值将列表划分为两部分，一部分小于枢纽值，另一部分大于枢纽值，递归进行。

时间复杂度: 平均O(NlogN)，最好O(NlogN)，最坏O(N^2)
空间复杂度: O(logn)到O(n)

不稳定
"""

# 快速排序，pivot选择为待排序列表中的第一项
# 这种写法时间复杂度为O(NlogN)
def quickSort(alist, first=0, last=None):
    """
    first默认为0
    last=None时赋予last = len(alist)-1
    first和last都是索引
    """
    last = len(alist)-1 if last == None else last
    if first < last:
        # 找到分割点位置
        pivotvalue = alist[first]  # 基准值
        leftmark = first+1 # 左界    
        rightmark = last # 右界
        done = False

        while not done:
            # 下面这个while循环的两个判断条件不能交换
            # 向右移动左标记直到超过右标记或找到大于基准数的项
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue: 
                leftmark += 1
            # 向左移动右标记直到超过左标记或找到小于基准数的项
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark: 
                rightmark -= 1
            # 左标记小于右标记，交换并继续
            if leftmark < rightmark: 
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            else:
                done = True
        # 此时右标记为基准值应该插入的位置，交换右标记与基准值
        alist[first], alist[rightmark] = alist[rightmark], alist[first]
        # 分治
        quickSort(alist, first, rightmark-1) # 子列表[first, rightmark-1]
        quickSort(alist, rightmark+1, last) # 子列表[rightmark+1, last]

# 使用三位取中设置枢纽值实现快速排序
# 此代码实现空间复杂度较高（需要改进），时间复杂度为O(NlogN)
def quickSort1(alist):
    if len(alist) <= 1:
        return alist
    else:
        threelist = [alist[0], alist[-1], alist[len(alist) // 2]] # 第一，最末，中间元素组成的列表
        pivotvalue = sorted(threelist)[1]  # 3个数的中位数，枢纽值
        index = alist.index(pivotvalue)  # 确定枢纽值在原列表中的位置

        # 小于等于枢纽值的子序列
        left = quickSort1([l for l in (alist[:index] + alist[index+1:]) if l <= pivotvalue])
        # 大于枢纽值的子序列
        right = quickSort1([r for r in (alist[:index] + alist[index+1:]) if r > pivotvalue])

        return left + [pivotvalue] + right

# 三位取中(三路快排)的第二种实现
def quickSort2(alist, first=0, last=None):
    last = len(alist)-1 if last == None else last
    if first < last:
        #  从alist[first],alist[mid],alist[last]三个中挑选中间值，并将其移动到alist[first]
        mid = (first + last) // 2
        if alist[first] > alist[last]:
            alist[first], alist[last] = alist[last], alist[first]
        if alist[mid] > alist[last]:
            alist[mid], alist[last] = alist[last], alist[mid]
        if alist[first] < alist[mid]:
            alist[first], alist[mid] = alist[mid], alist[first]

        pivotvalue = alist[first]  # 基准值
        leftmark = first+1 # 左界    
        rightmark = last # 右界

        done = False
        while not done:
            # 向右移动左标记直到超过右标记或找到大于基准数的项
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            # 向左移动右标记直到超过左标记或找到小于基准数的项
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark: 
                rightmark = rightmark -1
            # 左标记小于右标记，交换并继续
            if leftmark < rightmark:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            else: 
                done = True
        # 此时右标记为基准值应该插入的位置，交换右标记与基准值
        alist[first], alist[rightmark] = alist[rightmark], alist[first]
        quickSort(alist, first, rightmark-1)
        quickSort(alist, rightmark+1, last)

# 三路快排 +  插入排序
# 可以设定当列表数小于某个值的时候使用插入排序，其他情况使用快速排序（当排序数组较小时，插入排序的效率要高于快速排序）
def quickSort3(alist, first=0, last=None):
    last = len(alist)-1 if last == None else last
    if (last - first + 1) < 10:
        insert_sort(alist, first, last)
        return
    mid = (first + last) // 2
    if alist[first] > alist[last]:
        alist[first], alist[last] = alist[last], alist[first]
    if alist[mid] > alist[last]:
        alist[mid], alist[last] = alist[last], alist[mid]
    if alist[first] < alist[mid]:
        alist[first], alist[mid] = alist[mid], alist[first]

    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if leftmark < rightmark:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
        else:
            done = True
    alist[first], alist[leftmark] = alist[leftmark], alist[first]
    quickSort3(alist, first, leftmark-1)
    quickSort3(alist, leftmark+1, last)

def insert_sort(alist, first, last):
    for i in range(first+1, last+1):
        cur = alist[i]
        pos = i
        while pos > first and cur < alist[pos-1]:
            alist[pos] = alist[pos-1]
            pos -= 1
        alist[pos] = cur

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)

    alist = [54,26,93,17,77,31,44,55,20]
    alist = quickSort1(alist)
    print(alist)

    alist = [54,26,93,17,77,31,44,55,20]
    quickSort2(alist)
    print(alist)

    alist = [54,26,93,17,77,31,44,55,20]
    quickSort3(alist)
    print(alist)