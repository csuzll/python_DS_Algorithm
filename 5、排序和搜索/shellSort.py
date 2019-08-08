# 希尔排序
"""
把元素按下标的增量序列分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，
每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

时间复杂度:O(NlogN)
空间复杂度:O(1)

不稳定
"""


# 希尔排序需要的插入排序
def gapInsertSort(alist, start, gap):
    """
    start: 子序列的起始位置 
    gap: 增量
    """
    for i in range(start+gap, len(alist), gap): # 从索引start+gap到最后一个元素进行插入
        currentValue = alist[i]
        position  = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position -= gap # 向前

        alist[position] = currentValue # 插入合适位置

# 希尔排序，使用不同的增量集
# 将增量从长度的一半开始，每次都将增量减半，直至1按照基本插入排序进行排序。
def shellSort(alist):
    increment = len(alist) // 2 # 增量的初值取列表长度的一半
    while increment > 0:
        for startposition in range(increment): # 子列表的起始点
            gapInsertSort(alist, startposition, increment) # 为每个子列表进行排序

        print("After increments of size", increment, "The list is", alist)

        increment = increment // 2 # 增量减半

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)


# 上述代码写为一个函数
def shellSort2(alist):
    gap = len(alist)

    while gap > 1:
        gap = gap // 2

        for i in range(gap, len(alist)):
            for j in range(i % gap, i, gap):
                if alist[i] < alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
shellSort2(alist)
print(alist)