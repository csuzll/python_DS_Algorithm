# 动态规划解决硬币问题

# 问题描述
"""
使用最少的硬币找零。
硬币种类:  1，5，10 和 25 分
"""

# 思路
"""
动态编程解决方案将从找零一分钱开始，并系统地找到我们需要的找零额。
这保证我们在算法的每一步，已经知道为任何更小的数量进行找零所需的最小硬币数量。
"""

def dpMakeChange(coinValueList, change, minCoins):
    """
    coinValueList: 一个有效硬币值的列表
    change: 找零额
    minCoins: 一个包含每个值所需最小硬币数量的列表，初始化为全0
    """
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j]+1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]

print(dpMakeChange([1,5,10,25], 63, [0]*64))

# 改进，跟踪最小找零使用的硬币
# 为每个条目添加的最后一个硬币到coinsUsed列表。如果我们知道添加的最后一个硬币值，
# 我们可以简单地减去硬币的值，在表中找到前一个条目，找到该金额的最后一个硬币。我们可以通过表继续跟踪，直到我们开始的位置。
def dpMakeChange2(coinValueList, change, minCoins, coinsUsed):
    """
    coinValueList: 一个有效硬币值的列表
    change: 找零额
    minCoins: 一个包含每个值所需最小硬币数量的列表，初始化为全0
    coinsUsed: 用于找零的硬币列表, 初始化为全0
    """
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1 # 初始化为1，因为硬币最小值是1
        for j in [c for c in coinValueList if c<= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]

# 打印出使用的每个硬币的值
def printCoins(coinsUsed, change):
    """
    change: 找零额
    coinsUsed: 用于找零的硬币列表
    """
    coin = change

    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25] # 有效硬币值的列表
    coinsUsed = [0] * (amnt+1) # 用于找零的硬币列表
    coinCount = [0] * (amnt+1) # 与列表中的位置相对应进行找零的最小硬币数

    print("Making change for", amnt, "requires")
    print(dpMakeChange2(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are: ")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows: ")
    print(coinsUsed)

if __name__ == '__main__':
    main()
