# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = set([])
        nums.add(head.val)
        cur = head
        cur_next = head.next
        while cur_next:
            if cur_next.val in nums:
                cur.next = cur_next.next
                del cur_next
                cur_next = cur.next
            else:
                nums.add(cur_next.val)
                cur = cur.next
                cur_next = cur_next.next
        return head


