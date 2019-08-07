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
# 通过设置exchange是否交互标志
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