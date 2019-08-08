#  桶排序
"""
桶排序是将数组分到有限数量的桶里。
每个桶再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。

时间复杂度: 平均O(N+k)，最好O(N+k), 最坏O(N^2)
空间复杂度: O(N+k)

稳定
"""

# 基础桶排序
def bucketSort(alist, defaultBucketSize=5):
	maxVal, minVal = max(alist), min(alist)
	bucketSize = defaultBucketSize # 如果没有指定桶的容量，则默认为5
	bucketCount = (maxVal - minVal) // bucketSize + 1 # 数据分为 bucketCount 组

	buckets = [[] for _ in range(bucketCount)] # bucketCount个桶

	#　利用函数映射将各个数据放入对应的桶中
	for num in alist:
		buckets[(num-minVal) // bucketSize].append(num)

	alist.clear() # 清空alist
    # 对每一个桶中的元素进行排序
	for bucket in buckets:
		# insertionSort(bucket) # 假设使用插入排序
		bucket.sort()
		alist.extend(bucket) # 将排序好的桶依次放入到 alist 中

alist = [54,26,93,17,77,31,44,55,20]
bucketSort(alist)
print(alist)


# 区间均匀分布的列表进桶排序
# 例如，元素均匀的分布在区间[0,1)上，可以将桶排序与其它排序方法结合使用。
# 如果序列的大小为n，就将[0,1)划分成n个相同大小的子区间(桶),然后将n个输入数分布到各个桶中。先对各个桶中的数进行排序，然后按照次序把各桶中的元素列出来即可。
def bucketSort2(alist):
	n = len(alist)

	# 创建n个桶
	buket = [[] for _ in range(n)]

	# 把alist[i]插入到bucket[n * alist[i]]中
	for data in alist:
		index = int(data * n)
		buket[index].append(data)

	# 桶内排序(这里也可自定义为任何排序)
	for i in range(n):
		buket[i].sort()

	# 产生新的排序后的列表
	sortindex = 0
	for i in range(n):
		for j in range(len(buket[i])):
			alist[sortindex] = buket[i][j]
			sortindex += 1

array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucketSort2(array)
print(array)
