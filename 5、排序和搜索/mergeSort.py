# 归并排序(递归实现)

def mergeSort(alist):
    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        #  注意：使用切片的方式空间复杂度较高，这里需要改进
        lefthalf = alist[:mid] # 左半部分列表
        righthalf = alist[mid:] # 右半部分列表

        # 分别对左半部分和右半部分继续划分
        mergeSort(lefthalf) 
        mergeSort(righthalf)


        # 排序子序列，并合并
        i = 0
        j = 0
        k = 0 
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