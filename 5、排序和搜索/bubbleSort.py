# 冒泡排序
"""
遍历n-1遍要排序的数列，一次比较两个元素，如果他们的顺序错误就交换这两个元素。

时间复杂度: 平均O(N^2)，最好O(N), 最坏O(N^2)
空间复杂度: O(1)

稳定
"""

# 实现冒泡排序(in place)
def bubbleSort(alist):
    # 进行len(alist)-1轮遍历完成排序
    for passnum in range(len(alist)-1, 0, -1): 
        # passnum表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(passnum): 
            if alist[i] > alist[i+1]:
                # 在Python中，可以执行同时赋值。交换操作可以在一个语句中完成
                alist[i], alist[i+1] = alist[i+1], alist[i] 

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


# 改进冒泡排序，遍历期间没有交换，则认为已排序，可以停止。
# 通过设置exchange是否交换标志
def shortBubbleSort(alist):
    exchange = True # 是否交换标志 
    passnum = len(alist) - 1 # 最多进行len(alist)-1轮遍历就可以完成排序
    while passnum > 0 and exchange == True:
        exchange = False # 每一次遍历之前，将exchange设置为False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True # 本次遍历发生了交换，记录
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1

alist = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(alist)
print(alist)

# 改进冒泡排序2，记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubbleSort2(alist):
    length = len(alist) # 列表长度
    k = length # k为循环的范围，初值值为length
    for i in range(length):
        flag = True
        for j in range(1, k): # 只遍历到最后交换的位置即可
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
                k = j  # 记录最后交换的位置
                flag = False
        if flag:
            break    

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort2(alist)
print(alist)
