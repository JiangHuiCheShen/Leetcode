#给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#主要注意进位的问题
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    pre = ListNode(-1)
    now = pre
    nowl1 = l1
    nowl2 = l2
    jinwei = 0
    while nowl1 or nowl2:
        if nowl1:
            vall1 = nowl1.val
        else:
            vall1 = 0

        if nowl2:
            vall2 = nowl2.val
        else:
            vall2 = 0
        val = vall1 + vall2 + jinwei
        if val >= 10:
            now.next = ListNode(val % 10)
            jinwei = 1

        else:
            now.next = ListNode(val)
            jinwei = 0
        now = now.next
        if nowl1:
            nowl1 = nowl1.next

        if nowl2:
            nowl2 = nowl2.next

    if jinwei:
        now.next = ListNode(1)

    return pre.next


