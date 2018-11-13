# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        num = 0
        now = head
        while now:
            now = now.next
            num += 1
        mid = num // 2
        pre = ListNode(-1)
        head1 = pre

        while mid:
            temp = head.next
            head.next = head1
            head1 = head
            head = temp
            mid -= 1
        if num % 2 != 0:
            head = head.next
        while head:

            if head.val != head1.val:
                return False
            head = head.next
            head1 = head1.next
        return True

a=Solution()
lis=ListNode(1)
lis.next=ListNode(2)
b=a.isPalindrome(lis)