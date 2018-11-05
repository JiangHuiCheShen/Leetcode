class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    listl1 = []

    while l1:
        listl1.append(l1.val)
        l1 = l1.next
    while l2:
        listl1.append(l2.val)
        l2 = l2.next

    listl1.sort()
    pre = ListNode(-1)
    now = pre
    for i, val in enumerate(listl1):
        now.next = ListNode(val)
        now = now.next
    return pre.next