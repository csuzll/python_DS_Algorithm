# 归并排序
"""

归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，
每个子序列是有序的。然后再把有序子序列合并为整体有序序列。

时间复杂度: O(nlogn)
空间复杂度: O(1)

稳定
"""


# 归并排序(递归实现)

def mergeSort(alist):
    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        # 注意: 使用切片的方式空间复杂度较高，这里需要改进
        lefthalf = alist[:mid] # 左半部分列表
        righthalf = alist[mid:] # 右半部分列表

        # 分别对左半部分和右半部分继续划分
        mergeSort(lefthalf) 
        mergeSort(righthalf)


        # 排序子序列，并合并
        i = 0 # 左列表索引
        j = 0 # 右列表索引
        k = 0 # 总列表索引
        # i为左侧子列表的索引，j为右侧子列表的索引
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]: # 左侧列表的当前元素更小或一样大
                alist[k] = lefthalf[i]  # 将左侧列表的当前元素放入总列表
                i += 1 # 左侧列表索引右移一位
            else: # 右侧列表的当前元素更小
                alist[k] = righthalf[j] # 将右侧列表的当前元素放入总列表
                j += 1 # 右侧列表索引右移一位
            k += 1 # 总列表索引右移一位

        # 若某一子序列还剩余
        while i < len(lefthalf): # 左侧子列表未遍历完
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf): # 右侧子列表未遍历完
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print("Merging ", alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

### 改进归并排序，不使用切片操作，传递序号
def mergeSort2(alist, first=0, last=None):
    # 让下面递归传上来的元素个数不改变，而只是传递序号
    last = len(alist) if last==None else last

    print("Splitting: ", alist, "first: ", first, "last: ", last)

    # 子列表长度大于1
    if (last - first > 1):
        # 一分为二
        mid = (first + last) // 2
        mergeSort2(alist, first, mid) # 左部分
        mergeSort2(alist, mid, last) # 右部分

        # 排序子序列，并合并
        i = first # 左列表索引
        j = mid # 右列表索引
        tmplist = [] # 用来暂存合并的列表

        # 左右子序列比较
        while i < mid and j < last:
            if alist[i] <= alist[j]:
                tmplist.append(alist[i])
                i += 1
            else:
                tmplist.append(alist[j])
                j += 1
        # 左序列剩余
        while i < mid:
            tmplist.append(alist[i])
            i += 1
        # 右序列剩余
        while j < last:
            tmplist.append(alist[j])
            j += 1

        # 将tmplist数据复制到alist
        for tmpindex, index in enumerate(range(first, last)):
            alist[index] = tmplist[tmpindex]

        print("Merging: ", alist, "first: ", first, "last: ", last)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort2(alist)
print(alist)