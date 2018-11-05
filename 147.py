# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        ans = head

        left = head.next

        ans.next = None
        while left:
            insertnode = left
            left = left.next

            if insertnode.val < head:
                insertnode.next = ans
                ans = insertnode
            else:
                temp = ans.next
                pre = ans
                while insertnode.val >= temp.val and temp:
                    temp = temp.next
                    pre = pre.next

                pre.next = insertnode
                insertnode.next = temp

        return ans


sol=Solution()
a=ListNode(4)
b=ListNode(2)
c=ListNode(1)
a.next=b
b.next=c
ans=sol.insertionSortList(a)