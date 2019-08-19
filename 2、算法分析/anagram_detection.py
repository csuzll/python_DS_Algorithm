"""
易位词检测: 两个单词所含字母及其个数都是一样的，但是，字母的位置不一样。比如 abcc 和 cbca 就是 anagram.
"""
# 以下假设字母都是小写字母

# solution1
# 思路：检查长度是否相等，然后检查第一个字符串中的每个字符是否都出现在第二个字符串中
# 将str2转换为list，str1中的一个字符在list中出现，就将list那个字符替换为None
# 时间复杂度: O(N^2)
def anagramSolution1(s1, s2):
    if (len(s1) != len(s2)):
        stillOK = False

    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1

    return stillOK

# solution2
# 排序和比较：先将s1和s2转换为list后排序，然后进行对比
# 排序的时间复杂度是O(N^2)后者O(nlog n)，中间的迭代为O(N)，所以当n足够大时，整个算法的时间复杂度与排序的复杂度相同。
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

# solution3
# 蛮力法: 使用s1中的字符生成可能的字符串，再判断s2是否在这个生成的字符中
# 此算法实现困难，n个字符的字符串通过计算机能生成n!个候选字符串，n!远大于2^n

# solution4
# 计数和比较: 先统计26个字符在字符串中的次数，再比较
# 时间复杂度：T(n) = (n + n + 26)，所以O(n)=n。以空间换时间。
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK

if __name__ == '__main__':
    print(anagramSolution1("abcd", "dcba"))
    print(anagramSolution2('abcde','edcba'))
    print(anagramSolution4("apple", "pleap"))