# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_num = 0
        carry_num = 0
        cur_num += l1.val
        l1 = l1.next
        cur_num += l2.val
        l2 = l2.next
        ans = ListNode(cur_num % 10)
        cur_ans = ans
        carry_num = cur_num / 10
        while l1 or l2 or carry_num:
            cur_num = 0
            if l1:
                cur_num += l1.val
                l1 = l1.next
            if l2:
                cur_num += l2.val
                l2 = l2.next
            cur_num += carry_num
            carry_num = cur_num / 10
            cur_ans.next = ListNode(cur_num % 10)
            cur_ans = cur_ans.next
        return ans
            
if __name__ == '__main__':
    l1 = ListNode(2)
    l1_cur = l1
    l1_cur.next = ListNode(4)
    l1_cur = l1_cur.next
    l1_cur.next = ListNode(3)
    l1_cur = l1_cur.next
    
    l2 = ListNode(5)
    l2_cur = l2
    l2_cur.next = ListNode(6)
    l2_cur = l2_cur.next

    solution = Solution() 
    ans = solution.addTwoNumbers(l1, l2)
    while ans:
        print ans.val
        ans = ans.next
