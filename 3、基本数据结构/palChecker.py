from deque import Deque

# 回文检查("Palindrome Checker")
def palChecker(astring):

    chardeque = Deque()
    
    for ch in astring:
        chardeque.addRear(ch) # 将字符串按照字符逐个载入双端队列

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        front_s = chardeque.removeFront()  # 弹出队首字符
        rear_s = chardeque.removeRear() # 弹出队尾字符
        if front_s != rear_s:  # 判断是否相等
            stillEqual = False

    return stillEqual

# 改写回文检测的代码，使得有空格也可以检测（忽略空格）
def palChecker2(astring):
    chardeque = Deque()

    # 将非空格的字符加入双端队列
    for ch in astring:
        if ch != " ":
            chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

if __name__ == '__main__':
    print(palChecker("lsdkjfskf"))
    print(palChecker("radar"))
    print(palChecker2("I PREFER PI"))