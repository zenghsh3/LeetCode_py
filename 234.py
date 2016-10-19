#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
The problem doesn't say can not modify linked list,
so reverse the latter half list
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        if count < 2:
            return True
        mid = count / 2
        cur = head
        i = 0
        while i < mid:
            cur = cur.next
            i += 1
        tail = cur
        cur = cur.next
        while cur:
            tmp = cur.next
            cur.next = tail
            tail = cur
            cur = tmp
        i = 0
        while i < mid:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
            i += 1
        return True

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(0)
    head.next = ListNode(1) 
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(0)
    print solution.isPalindrome(head)
