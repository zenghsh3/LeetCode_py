class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            ans = int(str(x)[::-1])
            if ans > 0x7fffffff:
                return 0
            return ans
        else:
            ans = int(str(x)[1:][::-1])
            if ans > 0x7fffffff:
                return 0
            return -ans
        
