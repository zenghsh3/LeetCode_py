class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = len(s) 
        power = 1
        base = ord('A') - 1
        while i > 0:
            i -= 1
            num = ord(s[i]) - base
            ans += num * power
            power *= 26
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = 'Z'
    print solution.titleToNumber(s)

