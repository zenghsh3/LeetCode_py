class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        flag = True
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                flag = False
                break
        return flag
