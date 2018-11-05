# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        now = head
        nums = 0
        while now:
            nums += 1
            now = now.next
        num = k % nums
        p1 = head
        while num:
            p1 = p1.next
            num -= 1
        p2 = head
        if p1==None:
            return head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        right = p2.next
        p2.next=None
        p1.next = head


        return right

s=Solution()
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
# a.next=b
b.next=c
c.next=d
e=s.rotateRight(a,1)