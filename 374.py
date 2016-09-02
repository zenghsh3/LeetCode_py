# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(n):
    if n == 6:
        return 0
    elif n < 6:
        return -1
    else:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        ans = (l + r) / 2
        while True:
            if guess(ans) == 0:
                return ans
            elif guess(ans) == 1:
                l = ans + 1
                ans = (l + r) / 2
            else:
                r = ans - 1
                ans = (l + r) / 2

if __name__ == '__main__':
    solution = Solution()
    print solution.guessNumber(10)
