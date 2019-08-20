# 双向冒泡排序（鸡尾酒排序）
# 即当一次从左向右的排序比较结束后，立马从右向左来一次排序比较。(同一轮遍历进行，但有先后)
# 循环次数为len(alist) / 2
# 加入停止标志，如果在一次检索中，未发生交换，说明已经排序完毕，可以停止剩余循环

def bidirectional_bubbleSort(alist):
    length = len(alist) # 列表长度
    i = 0 # 控制循环次数
    flag = True

    while i < length // 2 and flag == True:
        flag = False
        # 从左到右，大值后移
        for j in range(i, length-1-i):
            if alist[j] > alist[j+1]:
                flag = True # 交换则设置为True
                alist[j], alist[j+1] = alist[j+1], alist[j]
        # 判断是否进行逆向遍历
        if flag:
            flag = False
            # 从右到左，小值前移
            for j in range(length-2-i, i, -1):
                if alist[j] < alist[j-1]:
                    flag = True # 交换则设置为True
                    alist[j], alist[j-1] = alist[j-1], alist[j]
        i += 1

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    bidirectional_bubbleSort(alist)
    print(alist)