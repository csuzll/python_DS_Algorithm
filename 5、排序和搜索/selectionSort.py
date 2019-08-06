# 选择排序
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1): # 遍历轮数len(alist)-1
        positionOfMax = 0 # 最大元素位置，默认设置为0
        for location in range(1, fillslot+1): # 1到fillslot
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location # 更新最大元素位置
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot] # 最后一个元素和最大元素交换
        
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)