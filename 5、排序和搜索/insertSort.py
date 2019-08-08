# 插入排序
"""
将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序；
首先将第一个作为已经排好序的，然后每次从后面取出插入到前面并排序。

时间复杂度:O(N^2)
空间复杂度:O(1)

稳定
"""


# 基本插入排序
def insertionSort(alist):
    """
    第一层循环控制循环次数，第二层循环比较元素，并向后移动元素供待插入元素插入
    """
    for index in range(1, len(alist)): # 从索引1到列表最后一个元素逐个插入
        currentvalue = alist[index] # 当前要插入的数
        position = index

        # 将当期元素与前一个元素比较
        while position > 0 and currentvalue < alist[position-1]: 
            alist[position] = alist[position - 1] # 比待插入元素大的元素都要向右(后)移
            position -= 1 # 向前

        alist[position] = currentvalue # 合适的位置插入元素

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


# 改进，折半插入(利用二分查找法来减少比较的次数)
def insertionSort2(alist):
    """
    外层循环控制循环次数，
    内层循环第一个确定待插入的位置与范围，
    内层循环第二个向后挪动元素的位置，插入待插入元素
    """
    # 从索引1到列表最后一个元素逐个插入
    for index in range(1, len(alist)):
        currentvalue = alist[index] # 当前要插入的数
        left = 0 # 左引用
        right = index - 1 # 右引用

        # 待插入的值与已排序区域的中间值比较，不断缩小区域范围，直到left和right相遇
        while left <= right:
            mid = (left + right) // 2
            if currentvalue < alist[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # 当left和right相遇时，待插入的位置为left所指的位置
        # 此时要将left到有序序列的最后一个元素都向后移动一个位置
        for j in range(index-1, left-1, -1):
            alist[j+1] = alist[j]
            
        # 插入元素(left与index相等说明插入值为插入末尾)
        if left != index:
            alist[left] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort2(alist)
print(alist)