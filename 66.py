class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            if digits[i] + carry > 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
                break
            i -= 1
        if carry:
            digits.insert(0, 1)
        return digits
