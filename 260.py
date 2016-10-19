class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = 0
        for x in nums:
            ans = x ^ ans
        tmp = ans
        diff = 1
        while tmp:
            if tmp & 1:
                break
            tmp = tmp >> 1
            diff = diff << 1
        a = ans
        b = ans
        for x in nums:
            if x & diff:
                a = a ^ x
            else:
                b = b ^ x
        return [a, b]

        
