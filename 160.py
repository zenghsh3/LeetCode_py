# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lenA = 0
        lenB = 0
        cur = headA
        while cur:
            lenA += 1
            cur = cur.next
        cur = headB
        while cur:
            lenB += 1
            cur = cur.next
        if lenA > lenB:
            i = lenA - lenB
            while i:
                headA = headA.next
                i -= 1
        if lenB > lenA:
            i = lenB - lenA
            while i:
                headB = headB.next
                i -= 1

        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None




