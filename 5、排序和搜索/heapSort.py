# 堆排序
"""
它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。构造堆结构。

时间复杂度: 平均，最好，最坏都是O(NlogN)
空间复杂度: O(1)

不稳定
"""


# 堆排序步骤
"""
1、构造最大堆: 若数组下标范围为0~n-1，考虑到单独一个元素是大根堆，则从下标(n//2)开始，递增的元素均为大根堆。
于是只要从(n//2-1)开始，递减向前依次调整构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。
2、堆排序: 由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆数组有序化。
思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0…n-2]做最大堆调整。
第二次将heap[0]与heap[n-2]交换，再对heap[0…n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。
由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。
3、最大堆调整: 该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点 。
"""

# 我的理解: 传递进来的列表无序，先通过调整构建成最大堆列表(此时还是无序，相当于二叉树的插入操作)，
# 然后进行堆排序(在最大堆列表上将根(0处)和从n-1开始直到1的结点值交换，每一次交换最大堆被破坏，重新调整维持最大堆)，这就得到了一个有序的列表了。

# 堆排序
def heapSort(alist):
    length = len(alist)

    first = length // 2 - 1 # 最后一个 非叶子结点

    # 构建最大堆
    for start in range(first, -1, -1):
        heapify(alist, start, length-1)

    # 堆排序，将最大堆转换为有序数组
    for end in range(length-1, 0, -1):
        # 将根结点元素与最后的叶子结点进行互换，取出最大根结点元素
        alist[end], alist[0] = alist[0], alist[end]
        heapify(alist, 0, end-1) # 取end-1是为了忽略交换后最后最大叶节点元素alist[length-1]

# 调整最大堆: 将堆的末端子节点作调整，使得子节点永远小于父节点
# 即以start为根结点的堆调整为最大堆
def heapify(alist, start, end):
    """
    start: 当前需要调整的位置 
    end: 调整边界（数组长度减1）
    """
    root = start 

    while True:
        child = 2 * root + 1 # 左孩子,child+1就是右孩子
        if child > end: # 判断是否存在child结点
            break
        if child + 1 <= end and alist[child] < alist[child+1]: # 找出左右孩子节点较大的
            child = child +1 
        # 判断是否为大顶堆(else的时候是最大堆)
        if alist[root] < alist[child]: # 较大的子结点成为父结点
            alist[root], alist[child] = alist[child], alist[root] # 交换
            root = child # 此刻的根结点下移，向下比较
        else:
            break

alist = [54,26,93,17,77,31,44,55,20]
heapSort(alist)
print(alist)