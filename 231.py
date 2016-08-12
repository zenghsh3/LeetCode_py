class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n & 1:
                return False
            n = n >> 1
        return True

if __name__ == '__main__':
    solution = Solution()
    n = 0
    print solution.isPowerOfTwo(n)
