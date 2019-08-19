"""最大相连子序列的和"""

# 算法1：时间复杂度为 n的3次方
def maxSubSum1(intnumlist):
    if(len(intnumlist)==0):
        return "序列为空"
    else:
        maxSum = 0
        for i in range(len(intnumlist)):
            for j in range(i, len(intnumlist)):
                thissum = 0;
                for k in range(i, j+1):
                    thissum+=intnumlist[k]

                if(thissum>maxSum):
                    maxSum = thissum
        return maxSum

# 算法2: 时间复杂度为n的2次方
def maxSubSum2(intnumlist):
    if(len(intnumlist)==0):
        return "序列为空"
    else:
        maxSum = 0
        for i in range(len(intnumlist)):
            thissum = 0
            for j in range(i, len(intnumlist)):
                thissum += intnumlist[j]
                if(thissum>maxSum):
                    maxSum = thissum
        return maxSum

# 算法3：时间复杂度为nlogn
# 这个算法存在一些问题，intnumlist的长度必须为偶数，奇数则不可行。
def maxSubSum3(intnumlist):
    return maxSumRec(intnumlist, 0, len(intnumlist)-1)

def maxSumRec(intnumlist, left, right):
    if(left == right):
        if(intnumlist[left]>0):
            return intnumlist[left]
        else:
            return 0

    center = (left+right)//2
    maxLeftSum = maxSumRec(intnumlist, left, center)
    maxRightSum = maxSumRec(intnumlist, center+1, right)

    maxLeftBorderSum, leftBorderSum = 0, 0
    # 倒序相加
    for i in range(left, center+1)[::-1]:
        leftBorderSum += intnumlist[i]
        if(leftBorderSum>maxLeftBorderSum):
            maxLeftBorderSum = leftBorderSum
    maxRightBorderSum, rightBorderSum = 0, 0
    # 正序相加
    for j in range(center+1, right+1):
        rightBorderSum += intnumlist[i]
        if(rightBorderSum>maxRightBorderSum):
            maxRightBorderSum = rightBorderSum

    return max([maxLeftSum, maxRightSum, maxLeftBorderSum+maxRightBorderSum])


# 算法4: 时间复杂度为n
def maxSubSum4(intnumlist):
    maxSum, thissum = 0, 0

    for i in range(len(intnumlist)):
        thissum += intnumlist[i]

        if(thissum > maxSum):
            maxSum = thissum
        if(thissum < 0):
            thissum = 0

    return maxSum

if __name__ == '__main__':
    num = [-2, 11, -4, 13, -5, -2]
    maxsum1 = maxSubSum1(num)
    maxsum2 = maxSubSum2(num)
    maxsum3 = maxSubSum3(num)
    maxsum4 = maxSubSum4(num)

    print(maxsum1)
    print(maxsum2)
    print(maxsum3)
    print(maxsum4)