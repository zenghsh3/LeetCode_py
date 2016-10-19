class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Reference:
            http://cwind.iteye.com/blog/2228443
        """
        ones = 0
        twos = 0
        threes = 0
        for x in nums:
            twos = twos | (ones & x)
            ones = ones ^ x
            threes = ones & twos
            ones = ones & (~threes)
            twos = twos & (~threes)
        return ones
