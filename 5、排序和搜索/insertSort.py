# 插入排序
def insertionSort(alist):
    for index in range(1, len(alist)): # 从索引1到列表最后一个元素逐个插入
        currentvalue = alist[index] # 当前要插入的数
        position = index

        while position > 0 and currentvalue < alist[position-1]: # 当前插入的数小于其前面的数
            alist[position] = alist[position - 1] # 比待插入元素大的元素都要向右(后)移
            position -= 1 # 向前

        alist[position] = currentvalue # 合适的位置插入元素

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


# 改进，折半插入