"""返回第k小的数，0<k<=len(alist)"""

# 第一种解法: 时间复杂度依赖于sort()，为O(nlogn)
def findksmall(alist, k):
    """
    :type alist: list
    :type k: int
    :rtype: num
    """
    if k > 0 and k <=len(alist):
        alist.sort()
        return alist[k-1]
    else:
        return None

# 第二种解法: 时间复杂度为O(n)
# 利用快排的思想
def findksmall2(alist, k):
    if k > 0 and k <= len(alist):
        key = alist[0]
        below = [s for s in alist if s < key] # 列表中小于key的数组成的列表
        above = [s for s in alist if s > key] # 列表中大于key的数组组成的列表
        i, j = len(below), len(alist) - len(above)

        if k-1 < i:
            return findksmall2(below, k)
        elif k-1 >= j:
            return findksmall2(above, k-j)
        else:
            # 不在below和above的中数为与key相等的数(i <= k-1 < j)
            return key
    else:
        return None

if __name__ == '__main__':
    list1 = [65,58,95,10,57,65,13,106,78,23,85]
    print(findksmall(list1, 5))
    list1 = [65,58,95,10,57,65,13,106,78,23,85]
    print(findksmall2(list1, 5))

