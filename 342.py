class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        powers = set([1,4,16,64,256,1024,4096,16384,65536,262144,1048576,4194304,16777216,67108864,268435456,1073741824])
        if num in powers:
            return True
        else:
            return False

    def findMaxPower(self):
        max_int = 0x7FFFFFFF
        ans = []
        for i in xrange(1000):
            if 4 ** i > max_int:
                break
            ans.append(str(4 ** i))
        print ','.join(ans)

if __name__ == '__main__':
    solution = Solution()
    print solution.findMaxPower()
