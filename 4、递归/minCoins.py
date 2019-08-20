# 找零问题中的优化问题。
# 最小硬币数

# 递归方法解答，速度非常慢
def recMC(coinValueList, change):
	# coinValueList: 硬币列表
	# change: 找零

	minCoins = change  # 令最小硬币数先等于找零
	if change in coinValueList: # 如果找零=某个硬币的价值，返回1
		return 1
	else:
		# 将硬币列表过滤为小于等于当前找零的硬币列表[c]用于迭代
		for coinValue in [c for c in coinValueList if c <= change]:
			# 递归调用
			numCoins = 1 + recMC(coinValueList, change-coinValue)
			if numCoins < minCoins:
				minCoins = numCoins

	return minCoins

# 优化，保存任意找零的硬币的最小数量在表中
# 这种方法应该叫做记忆化或者缓存的技术。
def recDC2(coinValueList, change, knownResults):
	# coinValueList: 硬币列表
	# change: 找零
	# knownResults: 找零硬币最小列表 

	minCoins = change
	if change in coinValueList:
		knownResults[change] = 1
		return 1
	elif knownResults[change] > 0:
		return knownResults[change]
	else:
		for coinValue in [c for c in coinValueList if c <= change]:
			numCoins = 1 + recDC(coinValueList, change - coinValue, knownResults)
			if numCoins < minCoins:
				minCoins = numCoins
				knownResults[change] = minCoins

	return minCoins

if __name__ == '__main__':
	print(recMC([1,5,10,25], 63))
	print(recDC2([1,5,10,25], 63, [0]*64))