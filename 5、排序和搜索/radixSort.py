# 基数排序
"""
基数排序有两种方法：

MSD （主位优先法）：从高位开始进行排序
LSD （次位优先法）：从低位开始进行排序

将整数按位数切割成不同的数字，然后按每个位数分别比较。将原数字放入桶中，再取出进行下一次比较。

时间复杂度: 平均O(N*k)，最好O(N*k), 最坏O(N*k)
空间复杂度: O(N+k)

稳定
"""


# 下面这个算法只针对正整数列表。(LSD次位优先)
def radixSort(alist):
	mod = 10
	div = 1
	mostBit = len(str(max(alist))) # 最大数的位数决定了外循环多少次

	buckets = [[] for _ in range(mod)] # 构造mod个桶

	while mostBit:
		# 将数据放入对应的桶中
		for num in alist:
			buckets[num // div % mod].append(num)

		# 从桶中取出放回原来的列表
		sortindex = 0 # alist的索引
		for bucket in buckets: 
			while bucket:
				alist[sortindex] = bucket.pop(0) # 依次取出
				sortindex += 1
		div *= 10
		mostBit -= 1

alist = [54,26,93,17,77,31,44,55,20]
radixSort(alist)
print(alist)
