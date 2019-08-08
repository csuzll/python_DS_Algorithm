# 计数排序

# 第一种: 待排序的数值作为计数列表的下标，统计每个数值的个数，然后依次输出。
def countSort(alist):
    length = len(alist)  # 列表长度
    maxvalue = max(alist) # 列表最大值
    count = [0] * (maxvalue+1) # 构造计数数组，长度为maxvalue+1
    sortedIndex = 0 # 索引

    # 将alist中的每个数作为count的下标，count的值为每个下标在原列表中出现的次数
    for i in range(length):
        count[alist[i]] += 1

    # 将count中值大于0的索引按顺序输出即为排序
    for i in range(maxvalue+1):
        while count[i] > 0:
            alist[sortedIndex] = i
            sortedIndex += 1
            count[i] -= 1
    return alist

alist = [54,26,93,17,77,31,44,55,20]
countSort(alist)
print(alist)



# 第二种: 给定的输入序列中的每一个元素x，确定该序列中值小于等于x元素的个数，然后将x直接存放到最终的排序序列的正确位置上。
def countSort2(alist, maxValue):
    length = len(alist) # 原列表的长度

    temp = [0 for i in range(maxValue+1)] # 中间列表

    result = [0 for i in range(length)] # 结果列表

    # 第一次遍历alist：统计alist中每个元素出现的次数，存入temp中
    for i in alist:
        temp[i] += 1

    # 第二次遍历temp：统计出小于等于当前下标的元素个数
    for i in range(1, maxValue+1):
        temp[i] = temp[i] + temp[i-1] # 当前值加前一个的值

    # 第三次遍历alist：找到该元素值在中间数组的对应下标，以这个中间数组的值作为结果数组的下标，将该元素存入结果数组
    for i in alist: # i为元素
        result[temp[i]-1] = i
        temp[i] -= 1

    return result

alist = [54,26,93,17,77,31,44,55,20]
print(countSort2(alist, 93))