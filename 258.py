class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        ans = num % 9
        if ans == 0:
            ans = 9
        return ans

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        while len(s) > 1:
            num = 0
            for i in xrange(len(s)):
                num += int(s[i])
            s = str(num)
        return int(s)

if __name__ == '__main__':
    solution = Solution()
    for i in range(10000):
        if solution.addDigits(i) != solution.addDigits2(i):
            print i
