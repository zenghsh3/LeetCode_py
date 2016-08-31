# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n += 1
        delete_n = head
        cur = head
        while cur and n:
            cur = cur.next
            n -= 1
        if n > 0:
            return head.next

        while cur:
            cur = cur.next
            delete_n = delete_n.next

        delete_n.next = delete_n.next.next
        return head
             
