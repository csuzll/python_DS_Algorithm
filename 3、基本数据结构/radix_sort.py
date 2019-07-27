# 实现基数排序
from queue import Queue
def get_max_num_len(numlist):
    # 给出数字列表中的位数最多的数的位数。
    max_len = 0
    for num in numlist:
        cur_len = len(str(num))
        if cur_len > max_len:
            max_len = cur_len
    return max_len

def get_num_by_order(num, order):
    # order为位数的序号
    # 比如456:6的order为1,5的order为2,4的order为3
    # 此函数按给定的order返回num相应位上的数字
    n = num // (10 ** (order - 1))
    return n % 10

def radix_sorting_machine(numlist):
    bins = []
    # 10个bin，每个bin都是一个队列
    for i in range(10):
        bins.append(Queue())

    # 按最大位数数量循环放置num到相应的bin中
    for i in range(get_max_num_len(numlist)):
        # 将每个num放到相应的bin中
        for num in numlist:
            bins[get_num_by_order(num, i+1)].enqueue(num)
        # 按顺序将bins中的数重新放回numlist中
        j = 0
        for bin in bins:
            while not bin.isEmpty():
                numlist[j] = bin.dequeue()
                j = j + 1
    # 最后就是返回已经从小到大排好序的数字list了。           
    return numlist

print(get_max_num_len([10, 20, 300]))
print(get_num_by_order(876, 2))
print(get_num_by_order(876, 4))
print(radix_sorting_machine([10, 20, 300]))
print(radix_sorting_machine([20, 1, 3, 677, 98, 25]))