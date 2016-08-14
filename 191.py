class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n & 1
            n = n >> 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print solution.hammingWeight(11)
