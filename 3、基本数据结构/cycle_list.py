# 链表有环的问题

class ListNode(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def traverse(self):
        temp = self
        while temp!=None:
            print(temp.data)
            temp = temp.next

# 在链表中构造环路
def cycle_list(mylist):
    first = mylist
    temp = first
    for i in range(3): # 向后移动3次
        temp = temp.next
    while first.next:
        first = first.next
    first.next = temp
    return mylist

# 检查链表是否存在环路
"""
通过两个指针，分别从链表的头节点出发，一个每次向后移动一步，另一个移动两步，
两个指针移动速度不一样，如果存在环，那么两个指针一定会在环里相遇。
"""
def check_cycle(mylist):
    slow = fast = mylist
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            return True
    return False

# 如果链表存在环，找到环的入口，链表头到环入口的长度
"""
由上个函数可知，按照 p2 每次两步，p1 每次一步的方式走，发现 p2 和 p1 重合，确定了单向链表有环路了。
接下来，让p2回到链表的头部，重新走，每次步长走1，那么当 p1 和 p2 再次相遇的时候，就是环路的入口了。
"""
def check_cycle_entrance(mylist):
    slow = fast = mylist
    found_cycle = False
    while fast != None and fast.next != None and not found_cycle:
        fast = fast.next.next
        slow = slow.next
        if slow is fast: # 链表有环路
            found_cycle = True
    if found_cycle:
        count = 1
        fast = mylist # 快指针从头结点开始，一次走一步
        while fast != slow:
            fast = fast.next
            slow = slow.next
            count += 1
        return fast, count
    else:
        return None

# 如果链表存在环，计算环的长度
"""
由上上个函数可知，按照 p2 每次两步，p1 每次一步的方式走，发现 p2 和 p1 重合，确定了单向链表有环路了。
接下来，从相遇点继续走，那么当 p1 和 p2 再次相遇的时候，p1走过的长度即为环长度。
"""
def count_cycle_length(mylist):
    slow = fast = mylist
    found_cycle = False
    while fast != None and fast.next != None and not found_cycle:
        fast = fast.next.next
        slow = slow.next
        if slow is fast: # 链表有环路
            found_cycle = True
    if found_cycle:
        count = 1
        fast = fast.next.next
        slow = slow.next
        while fast != slow: # 第二次相遇
            fast = fast.next.next
            slow = slow.next
            count += 1
        return count
    else:
        return None

# 如果链表存在环，计算链表的长度
"""
链表起点到环入口的长度 + 链表环的长度 = 链表长度
"""

# 给出两个单向链表的头指针，求链表的交点
"""
求出两链表的长度，长链表先走，然后逐个比较两个链表的值，第一个相等的值即为交点。
（若只要判断是否相交，只需判断尾节点是否相等）　　
"""
def linkedlist_node(mylist1, mylist2):
    head1 = mylist1
    head2 = mylist2
    length1=length2=0
    while head1:
        length1 = length1+1
        head1 = head1.next
    while head2:
        length2 = length2+1
        head2 = head2.next    
    if length1>length2:  # 长链表先走
        for i in range(length1-length2):
            mylist1 = mylist1.next
    else:
        for i in range(length2-length1):
            mylist2 = mylist2.next
    while mylist1!=None and mylist2!=None:
        if mylist1.data == mylist2.data: # 应该是mylist1==mylist2（或mylist1 is mylist2）,这里使用值代替了，方便看执行结果
            return mylist1.data
        mylist1 = mylist1.next
        mylist2 = mylist2.next
    return None

if __name__ == '__main__':
    l1 = ListNode(1,ListNode(56,ListNode(8,ListNode(20,ListNode(10,ListNode(12))))))
    l2 = ListNode(31,ListNode(26,ListNode(18,ListNode(32))))
    l3 = cycle_list(l1) # 有环
    
    print(check_cycle(l2)) # False
    print(check_cycle(l3)) # True

    cycle_node, a_len = check_cycle_entrance(l3)
    print(cycle_node.data) # 20
    print(a_len) # 4

    cycle_node2 = check_cycle_entrance(l2)
    print(cycle_node2) # None

    cycle_length = count_cycle_length(l3)
    print(cycle_length) # 3

    print(a_len + cycle_length) # 7

    l1 = ListNode(1,ListNode(56,ListNode(8,ListNode(20,ListNode(10,ListNode(12))))))
    l2 = ListNode(31,ListNode(25,ListNode(10,ListNode(12))))
    print(linkedlist_node(l1, l2)) # 10