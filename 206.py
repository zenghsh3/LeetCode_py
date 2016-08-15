import ipdb
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        ans = head
        head = head.next
        ans.next = None
        while head:
            tmp = ans
            ans = head
            head = head.next
            ans.next = tmp
        return ans

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solution = Solution()
    ans = solution.reverseList(head)
    while ans:
        print ans.val
        ans = ans.next


