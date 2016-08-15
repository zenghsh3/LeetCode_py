# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next  = ListNode(2)
    head.next.next  = ListNode(3)

    solution.deleteNode(head.next)
    while head:
        print head.val
        head = head.next
