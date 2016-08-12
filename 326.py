import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if str(math.log(n, 3))[-2:] == '.0':
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    n = 243 * 243
    print solution.isPowerOfThree(n)
