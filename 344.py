class Solution(object):
        def reverseString(self, s):
            """
            :type s: str
            :rtype: str
            """
            return s[::-1]

if __name__ == '__main__':
    solution = Solution()
    s = 'abcd'
    print solution.reverseString(s)
