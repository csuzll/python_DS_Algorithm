# 希尔排序
"""
从增量的初始值选取，到逐渐变为1，将所有用过的增量组成一个序列，就是增量序列。

给定一个增量序列[a1,a2,...,an]，增量序列最后一个元素an=1。
首先以a1为增量，对列表分组，每个分组进行排序(一般是插入排序)。
然后以a2为增量，对列表分组，每个分组进行排序。
直到以1为增量，整个列表恰被分成一组，插入排序后算法便终止。

时间复杂度:平均O(NlogN)到O(N^2)之间，最好O(N), 最坏O(N^2)
空间复杂度:O(1)

希尔增量序列: [N//2, (N//2)//2, ..., 1]

Hibbard增量的递推公式：H(1) = 1, H(i)=2*H(i-1)+1。即是[1, 3, 7, ... , 2ⁿ-1]
这个增量的特点是增量没有公因子。
初始增量2ⁿ-1中的n等于log(n+1)取整。
使用Hibbard增量的希尔排序的最坏情形运行时间为θ(N^(3/2))。

不稳定
"""

# 希尔排序需要的插入排序
def gapInsertSort(alist, start, gap):
    """
    start: 子序列的起始位置 
    gap: 增量
    """
    # start+gap为子序列中的第二个数，第一个数假定有序了。
    for i in range(start+gap, len(alist), gap): # 从索引start+gap到最后一个元素进行插入
        currentValue = alist[i]
        position  = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position -= gap # 向前

        alist[position] = currentValue # 插入合适位置

# 希尔排序，使用不同的增量序列
# 将增量从长度的一半开始，每次都将增量减半，直至1按照基本插入排序进行排序。
def shellSort(alist):
    increment = len(alist) // 2 # 增量的初值取列表长度的一半
    while increment > 0:
        for startposition in range(increment): # 子列表的起始点
            gapInsertSort(alist, startposition, increment) # 为每个子列表进行排序

        print("After increments of size", increment, "The list is", alist)

        increment = increment // 2 # 增量减半


# 希尔排序另一种写法
def shellSort1(alist):
    gap = len(alist)

    while gap > 1:
        gap = gap // 2

        for i in range(gap, len(alist)): # 从gap到最后一个元素
            for j in range(i % gap, i, gap):
                if alist[i] < alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]

# 使用Hibbard增量实现希尔排序
def shellSort2(alist):
    length = len(alist)
    gap = 1
    while gap < length // 2:
        gap = gap * 2 + 1 # 动态定义间隔序列
    while gap > 0:
        for i in range(gap, length):
            curNum = alist[i] # curNum 保存当前待插入的数
            preIndex = i - gap
            while preIndex >=0 and curNum < alist[preIndex]: 
                alist[preIndex+gap] = alist[preIndex] # 将比 curNum 大的元素向后移动
                preIndex -= gap
            alist[preIndex+gap] = curNum # 待插入的数的正确位置
        gap //= 2  # 下一个动态间隔

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    shellSort(alist)
    print(alist)

    alist = [54,26,93,17,77,31,44,55,20]
    shellSort1(alist)
    print(alist)

    alist = [54,26,93,17,77,31,44,55,20]
    shellSort2(alist)
    print(alist)