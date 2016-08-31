class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        ans = str(self.factorial(n))
        i = len(ans) - 1
        zeros = 0
        while i >= 0:
            if ans[i] == '0':
                zeros += 1
                i -= 1
            else:
                break
        return zeros
        """
        exp = 0
        while 5 ** exp < n:
            exp += 1

        ans = 0
        i = 1
        while i <= exp:
            ans += n / (5 ** i)
            i += 1
        
        return ans

    """
    def factorial(self, n):
        ans = 1
        while n > 1:
            ans *= n
            n -= 1
        return ans
    """

if __name__ == '__main__':
    solution = Solution()
