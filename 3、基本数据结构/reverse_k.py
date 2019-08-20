# 链表的复杂倒转
# 给出一个链表和一个数k，比如，链表为1→2→3→4→5→6，k=2，则翻转后2→1→6→5→4→3，
# 若k=3，翻转后3→2→1→6→5→4，若k=4，翻转后4→3→2→1→6→5，用程序实现。

class ListNode:
    def __init__(self, data, n=None):
        self.data = data
        self.next = n

    def traverse(self):
        temp = self
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

# 一般链表倒转
def reverse(head):
    prev = head
    cur = prev.next
    prev.next = None
    while cur != None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    # 返回prev为新链表的头，head为新链表的尾
    return prev, head

# 复杂倒转
def reverse_k(head, k):
    temp = head
    for i in range(k-1):
        temp = temp.next
        if temp==None:
            return None
    mid = temp.next
    temp.next=None
    head1,end1 = reverse(head)
    head2,end2 = reverse(mid)
    end1.next = head2
    return head1

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(56, ListNode(8, ListNode(20, ListNode(10, ListNode(12))))))
    l1.traverse()
    print("\n")

    l2 = reverse(l1)
    l2[0].traverse()
    print("\n")

    l1 = ListNode(1, ListNode(56, ListNode(8, ListNode(20, ListNode(10, ListNode(12))))))
    l3 = reverse_k(l1, 3)
    l3.traverse()