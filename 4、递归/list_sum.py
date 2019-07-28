# 计算list的和

# 常规: 迭代列表求和
def listsum(numlist):
    sum = 0
    for num in numlist:
        sum += num
    return sum

print(listsum([1,3,5,7,9]))


# 递归的思路
# listSum(numlist) = numlist[0] + listSum(numlist[1:])
# (1 + (3 + (5 + (7 + 9))))
def listSum(numlist):
    if len(numlist == 1):
        return numlist[0]
    else:
        return numlist[0] + listSum(numlist[1:])
    
print(listsum([1,3,5,7,9]))
